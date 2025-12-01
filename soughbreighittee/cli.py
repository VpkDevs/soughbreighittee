#!/usr/bin/env python3
"""
Soughbreighittee - Comprehensive Harm Reduction and Addiction Recovery App

Main command-line interface for exploring recovery methods for Opiate Use Disorder.
"""

import sys
import os
from typing import List, Optional
from datetime import datetime
import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.markdown import Markdown
from rich.text import Text
from rich.prompt import Prompt, Confirm
from rich.progress import Progress, SpinnerColumn, TextColumn

from . import __version__, EMERGENCY_CONTACTS, DISCLAIMER
from .models import MethodCategory, EvidenceLevel, SafetyLevel, AccessibilityLevel
from .database import (
    get_all_methods, get_methods_by_category, get_method_by_id,
    search_methods, get_crisis_resources, get_all_resources,
    get_database_stats, get_quick_info, get_daily_quote,
    get_coping_strategy, get_checkin_prompt, get_multiple_coping_strategies,
    calculate_sobriety_days, export_method_to_text, export_crisis_card,
    get_treatment_locators, search_methods_by_tags
)

console = Console()


# Safety level color mapping
SAFETY_COLORS = {
    SafetyLevel.SAFE: "green",
    SafetyLevel.MODERATE_RISK: "yellow",
    SafetyLevel.HIGH_RISK: "red",
    SafetyLevel.DANGEROUS: "bold red",
    SafetyLevel.UNKNOWN: "dim white"
}


def show_disclaimer():
    """Display the medical disclaimer."""
    disclaimer_panel = Panel(
        DISCLAIMER,
        title="[bold red]⚠️ MEDICAL DISCLAIMER ⚠️[/bold red]",
        border_style="red"
    )
    console.print(disclaimer_panel)
    console.print()


def show_emergency_contacts():
    """Display emergency contacts."""
    emergency_text = "\n".join([
        f"• {name}: [bold]{contact}[/bold]"
        for name, contact in EMERGENCY_CONTACTS.items()
    ])
    
    emergency_panel = Panel(
        emergency_text,
        title="[bold red]🆘 EMERGENCY CONTACTS 🆘[/bold red]",
        border_style="red"
    )
    console.print(emergency_panel)
    console.print()


def get_safety_styled(safety_level: SafetyLevel) -> str:
    """Get a styled string for safety level with appropriate color."""
    color = SAFETY_COLORS.get(safety_level, "white")
    level_text = safety_level.value.split(" - ")[0]
    
    if safety_level in [SafetyLevel.HIGH_RISK, SafetyLevel.DANGEROUS]:
        return f"[{color}]⚠️ {level_text} ⚠️[/{color}]"
    elif safety_level == SafetyLevel.SAFE:
        return f"[{color}]✓ {level_text}[/{color}]"
    else:
        return f"[{color}]{level_text}[/{color}]"


def display_method_summary(methods: List, show_hints: bool = True):
    """Display a table summary of methods."""
    if not methods:
        console.print("[yellow]No methods found matching your criteria.[/yellow]")
        return

    table = Table(show_header=True, header_style="bold magenta", title=f"📋 Found {len(methods)} method(s)")
    table.add_column("ID", style="dim")
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Category", style="green")
    table.add_column("Evidence", style="blue")
    table.add_column("Safety", style="yellow")
    table.add_column("Rating", justify="center")

    for method in methods:
        # Color code effectiveness rating
        effectiveness_color = "green" if method.effectiveness_rating >= 7 else "yellow" if method.effectiveness_rating >= 5 else "red"
        effectiveness = f"[{effectiveness_color}]{method.effectiveness_rating}/10[/{effectiveness_color}]"
        
        # Color code safety
        safety_color = SAFETY_COLORS.get(method.safety_level, "white")
        safety_text = method.safety_level.value.split(" - ")[0]
        if method.safety_level in [SafetyLevel.HIGH_RISK, SafetyLevel.DANGEROUS]:
            safety_display = f"[{safety_color}]⚠️ {safety_text}[/{safety_color}]"
        else:
            safety_display = f"[{safety_color}]{safety_text}[/{safety_color}]"
        
        # Truncate long names
        name_display = method.name if len(method.name) <= 35 else method.name[:32] + "..."
        
        table.add_row(
            method.id,
            name_display,
            method.category.value.split(" (")[0],  # Shorter category name
            method.evidence_level.value.split(" - ")[0],
            safety_display,
            effectiveness
        )

    console.print(table)
    
    if show_hints and methods:
        console.print()
        console.print("[dim]💡 Tip: Use 'python main.py show <id>' for detailed information about any method.[/dim]")
        console.print("[dim]💡 Tip: Use 'python main.py quick <id>' for quick key facts.[/dim]")


def display_method_detail(method_id: str):
    """Display detailed information about a specific method."""
    method = get_method_by_id(method_id)
    if not method:
        # Try searching
        results = search_methods(method_id)
        if results:
            method = results[0]
            console.print(f"[dim]Showing results for '{method.name}'[/dim]")
        else:
            console.print(f"[red]Error: Method '{method_id}' not found[/red]")
            console.print("[dim]Try using 'python main.py search <term>' to find methods.[/dim]")
            return

    # High-risk warning if applicable
    if method.safety_level in [SafetyLevel.HIGH_RISK, SafetyLevel.DANGEROUS]:
        warning_text = f"⚠️ WARNING: This method is classified as {method.safety_level.value}.\n"
        warning_text += "Please consult healthcare professionals before considering this approach."
        console.print(Panel(warning_text, title="[bold red]⚠️ SAFETY WARNING ⚠️[/bold red]", border_style="bold red"))
        console.print()

    # Main method information with styled header
    safety_color = SAFETY_COLORS.get(method.safety_level, "white")
    console.print(f"\n[bold cyan]{'═' * 60}[/bold cyan]")
    console.print(f"[bold cyan]  {method.name}[/bold cyan]")
    console.print(f"[bold cyan]{'═' * 60}[/bold cyan]")
    console.print(f"[dim]Category: {method.category.value}[/dim]")
    console.print(f"[dim]ID: {method.id}[/dim]\n")
    
    # Description
    console.print(Panel(method.description, title="📖 Description", border_style="cyan"))
    
    # How it works
    console.print(Panel(method.how_it_works, title="🔬 How It Works", border_style="blue"))
    
    # Key metrics table
    metrics_table = Table.grid(padding=1)
    metrics_table.add_column(style="bold")
    metrics_table.add_column()
    
    metrics_table.add_row("📊 Evidence Level:", f"[blue]{method.evidence_level.value}[/blue]")
    metrics_table.add_row("🛡️ Safety Level:", get_safety_styled(method.safety_level))
    
    # Color-coded effectiveness
    eff_color = "green" if method.effectiveness_rating >= 7 else "yellow" if method.effectiveness_rating >= 5 else "red"
    metrics_table.add_row("⭐ Effectiveness Rating:", f"[{eff_color}]{method.effectiveness_rating}/10[/{eff_color}]")
    metrics_table.add_row("🚪 Accessibility:", f"[green]{method.accessibility.value}[/green]")
    
    if method.typical_duration:
        metrics_table.add_row("⏱️ Typical Duration:", method.typical_duration)
    if method.cost_range:
        metrics_table.add_row("💰 Cost Range:", method.cost_range)
    if method.insurance_coverage:
        metrics_table.add_row("🏥 Insurance Coverage:", method.insurance_coverage)
    if method.success_rate:
        metrics_table.add_row("📈 Success Rate:", method.success_rate)
    
    console.print(Panel(metrics_table, title="📋 Key Information", border_style="magenta"))
    
    # Pros and Cons
    if method.pros or method.cons:
        pros_cons_table = Table.grid(padding=2)
        pros_cons_table.add_column("Pros", style="green")
        pros_cons_table.add_column("Cons", style="red")
        
        pros_text = "\n".join([f"✓ {pro}" for pro in method.pros]) if method.pros else ""
        cons_text = "\n".join([f"✗ {con}" for con in method.cons]) if method.cons else ""
        
        pros_cons_table.add_row(pros_text, cons_text)
        console.print(Panel(pros_cons_table, title="⚖️ Pros and Cons", border_style="yellow"))
    
    # Safety information with appropriate styling
    if method.risks_side_effects or method.contraindications:
        safety_content = ""
        if method.risks_side_effects:
            safety_content += "[bold]Risks and Side Effects:[/bold]\n"
            safety_content += "\n".join([f"• {risk}" for risk in method.risks_side_effects])
            safety_content += "\n\n"
        
        if method.contraindications:
            safety_content += "[bold]Contraindications (when NOT to use):[/bold]\n"
            safety_content += "\n".join([f"• {contra}" for contra in method.contraindications])
        
        border = "bold red" if method.safety_level in [SafetyLevel.HIGH_RISK, SafetyLevel.DANGEROUS] else "red"
        console.print(Panel(safety_content, title="[red]⚠️ Safety Information[/red]", border_style=border))
    
    # Who it's best for
    if method.best_for or method.not_recommended_for:
        suitability_content = ""
        if method.best_for:
            suitability_content += "[bold green]Best for:[/bold green]\n"
            suitability_content += "\n".join([f"• {item}" for item in method.best_for])
            suitability_content += "\n\n"
        
        if method.not_recommended_for:
            suitability_content += "[bold red]Not recommended for:[/bold red]\n"
            suitability_content += "\n".join([f"• {item}" for item in method.not_recommended_for])
        
        console.print(Panel(suitability_content, title="👥 Suitability", border_style="cyan"))
    
    # Requirements and where to find
    logistics_content = ""
    if method.requirements:
        logistics_content += "[bold]Requirements:[/bold]\n"
        logistics_content += "\n".join([f"• {req}" for req in method.requirements])
        logistics_content += "\n\n"
    
    if method.where_to_find:
        logistics_content += "[bold]Where to find:[/bold]\n"
        logistics_content += "\n".join([f"• {location}" for location in method.where_to_find])
    
    if logistics_content:
        console.print(Panel(logistics_content, title="Access Information"))
    
    # Combination information
    if method.can_combine_with or method.cannot_combine_with:
        combo_content = ""
        if method.can_combine_with:
            combo_content += "[bold green]Can combine with:[/bold green]\n"
            combo_content += "\n".join([f"• {item}" for item in method.can_combine_with])
            combo_content += "\n\n"
        
        if method.cannot_combine_with:
            combo_content += "[bold red]Cannot combine with:[/bold red]\n"
            combo_content += "\n".join([f"• {item}" for item in method.cannot_combine_with])
        
        console.print(Panel(combo_content, title="🔗 Combination Information", border_style="yellow"))
    
    # Resources
    if method.resources:
        resources_content = "\n".join([f"• {resource}" for resource in method.resources])
        console.print(Panel(resources_content, title="📚 Additional Resources", border_style="green"))
    
    # Footer
    console.print()
    console.print("[dim]═" * 60 + "[/dim]")
    console.print("[dim]⚠️ This information is for educational purposes only.[/dim]")
    console.print("[dim]Always consult healthcare providers for medical advice.[/dim]")


@click.group()
@click.version_option(__version__)
def cli():
    """
    Soughbreighittee - Comprehensive Harm Reduction and Addiction Recovery App
    
    A comprehensive tool for exploring recovery methods for Opiate Use Disorder.
    Get detailed information about all known recovery approaches, from evidence-based
    medical treatments to alternative and harm reduction strategies.
    
    \b
    🆘 If you are in crisis, call 988 or text HOME to 741741
    """
    pass


@cli.command()
def disclaimer():
    """Show the medical disclaimer and emergency contacts."""
    show_disclaimer()
    show_emergency_contacts()


@cli.command()
def emergency():
    """Show emergency contacts and crisis resources."""
    show_emergency_contacts()
    
    # Show crisis resources
    crisis_resources = get_crisis_resources()
    if crisis_resources:
        console.print("\n[bold]🆘 Crisis Resources:[/bold]\n")
        for resource in crisis_resources:
            resource_text = f"[bold cyan]{resource.title}[/bold cyan]\n"
            resource_text += f"{resource.description}\n"
            if resource.phone:
                resource_text += f"[bold]📞 Contact: {resource.phone}[/bold]"
            if resource.url:
                resource_text += f"\n[dim]🌐 {resource.url}[/dim]"
            console.print(Panel(resource_text, border_style="red"))
    
    # Show treatment locators
    locators = get_treatment_locators()
    if locators:
        console.print("\n[bold]🔍 Treatment Locators:[/bold]\n")
        for resource in locators:
            console.print(f"• [cyan]{resource.title}[/cyan]: {resource.url or resource.phone}")


@cli.command()
def resources():
    """Show all available resources including locators and organizations."""
    all_resources = get_all_resources()
    
    console.print("[bold]📚 All Available Resources[/bold]\n")
    
    # Group by type
    crisis = [r for r in all_resources if r.is_crisis_resource]
    locators = get_treatment_locators()
    others = [r for r in all_resources if not r.is_crisis_resource and r not in locators]
    
    if crisis:
        console.print("[bold red]🆘 Crisis Resources[/bold red]")
        for resource in crisis:
            contact = resource.phone if resource.phone else resource.url
            console.print(f"  • [cyan]{resource.title}[/cyan]: {contact}")
        console.print()
    
    if locators:
        console.print("[bold blue]🔍 Treatment Locators[/bold blue]")
        for resource in locators:
            console.print(f"  • [cyan]{resource.title}[/cyan]")
            if resource.url:
                console.print(f"    [dim]{resource.url}[/dim]")
        console.print()
    
    if others:
        console.print("[bold green]📖 Educational & Support Resources[/bold green]")
        for resource in others:
            console.print(f"  • [cyan]{resource.title}[/cyan]")
            if resource.url:
                console.print(f"    [dim]{resource.url}[/dim]")


@cli.command()
@click.option('--category', type=click.Choice([cat.name for cat in MethodCategory]), 
              help='Filter by category')
@click.option('--evidence', type=click.Choice([ev.name for ev in EvidenceLevel]),
              help='Filter by evidence level')
@click.option('--safety', type=click.Choice([sf.name for sf in SafetyLevel]),
              help='Filter by safety level')
@click.option('--accessibility', type=click.Choice([ac.name for ac in AccessibilityLevel]),
              help='Filter by accessibility')
@click.option('--min-effectiveness', type=int, help='Minimum effectiveness rating (1-10)')
def list(category, evidence, safety, accessibility, min_effectiveness):
    """List all available recovery methods with optional filters."""
    
    methods = get_all_methods()
    
    # Apply filters
    if category:
        category_enum = MethodCategory[category]
        methods = [m for m in methods if m.category == category_enum]
    
    if evidence:
        evidence_enum = EvidenceLevel[evidence]
        methods = [m for m in methods if m.evidence_level == evidence_enum]
    
    if safety:
        safety_enum = SafetyLevel[safety]
        methods = [m for m in methods if m.safety_level == safety_enum]
    
    if accessibility:
        accessibility_enum = AccessibilityLevel[accessibility]
        methods = [m for m in methods if m.accessibility == accessibility_enum]
    
    if min_effectiveness:
        methods = [m for m in methods if m.effectiveness_rating >= min_effectiveness]
    
    # Sort by effectiveness rating (descending)
    methods.sort(key=lambda x: x.effectiveness_rating, reverse=True)
    
    console.print(f"[bold]Found {len(methods)} recovery method(s)[/bold]\n")
    display_method_summary(methods)


@cli.command()
def categories():
    """List all method categories with counts."""
    console.print("[bold]Recovery Method Categories:[/bold]\n")
    
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Category", style="cyan")
    table.add_column("Count", style="green", justify="right")
    table.add_column("Description", style="white")
    
    category_descriptions = {
        MethodCategory.MEDICAL_ASSISTED_TREATMENT: "FDA-approved medications for OUD treatment",
        MethodCategory.BEHAVIORAL_THERAPY: "Counseling and psychological interventions",
        MethodCategory.SUPPORT_GROUPS: "Peer support and group recovery programs",
        MethodCategory.ALTERNATIVE_COMPLEMENTARY: "Non-conventional approaches and treatments",
        MethodCategory.HARM_REDUCTION: "Strategies to reduce risks without requiring abstinence",
        MethodCategory.CRISIS_EMERGENCY: "Immediate help and emergency interventions",
        MethodCategory.HOLISTIC_WELLNESS: "Whole-person approaches to recovery",
        MethodCategory.PEER_SUPPORT: "Support from others with lived experience"
    }
    
    for category in MethodCategory:
        methods_in_category = get_methods_by_category(category)
        description = category_descriptions.get(category, "")
        table.add_row(category.value, str(len(methods_in_category)), description)
    
    console.print(table)


@cli.command()
@click.argument('method_id')
def show(method_id):
    """Show detailed information about a specific method."""
    display_method_detail(method_id)


@cli.command()
@click.argument('query')
def search(query):
    """Search for recovery methods by keyword."""
    console.print(f"[bold]Searching for methods matching '{query}'...[/bold]\n")
    
    results = search_methods(query)
    
    if not results:
        console.print(f"[yellow]No methods found matching '{query}'.[/yellow]")
        console.print("\n[dim]Try searching for terms like: methadone, therapy, support, naloxone, acupuncture[/dim]")
        return
    
    display_method_summary(results)
    
    if len(results) == 1:
        console.print(f"\n[dim]Use 'soughbreighittee show {results[0].id}' for detailed information.[/dim]")
    else:
        console.print(f"\n[dim]Use 'soughbreighittee show <method_id>' for detailed information about any method.[/dim]")


@cli.command()
def compare():
    """Interactive method comparison tool."""
    console.print("[bold]Method Comparison Tool[/bold]\n")
    
    # Get methods to compare
    methods_to_compare = []
    
    while len(methods_to_compare) < 5:  # Limit to 5 for readability
        method_name = Prompt.ask(
            f"Enter method name or ID to compare ({len(methods_to_compare)} selected)"
            f"{'[press Enter to finish]' if methods_to_compare else ''}"
        )
        
        if not method_name and methods_to_compare:
            break
        
        if not method_name:
            console.print("[yellow]Please enter at least one method name.[/yellow]")
            continue
        
        # Try to find the method
        found_methods = search_methods(method_name)
        if not found_methods:
            console.print(f"[red]No methods found matching '{method_name}'[/red]")
            continue
        
        if len(found_methods) > 1:
            console.print(f"[yellow]Multiple methods found:[/yellow]")
            for i, method in enumerate(found_methods[:5]):
                console.print(f"{i+1}. {method.name}")
            
            choice = Prompt.ask("Select method number", choices=[str(i+1) for i in range(len(found_methods[:5]))])
            selected_method = found_methods[int(choice)-1]
        else:
            selected_method = found_methods[0]
        
        if selected_method not in methods_to_compare:
            methods_to_compare.append(selected_method)
            console.print(f"[green]Added {selected_method.name}[/green]")
        else:
            console.print("[yellow]Method already selected.[/yellow]")
    
    if not methods_to_compare:
        return
    
    # Create comparison table
    console.print(f"\n[bold]Comparing {len(methods_to_compare)} methods:[/bold]\n")
    
    comparison_table = Table(show_header=True, header_style="bold magenta")
    comparison_table.add_column("Attribute", style="cyan")
    
    for method in methods_to_compare:
        comparison_table.add_column(method.name[:20], style="white")  # Truncate long names
    
    # Add comparison rows
    attributes = [
        ("Category", lambda m: m.category.value),
        ("Evidence Level", lambda m: m.evidence_level.value.split(" - ")[0]),
        ("Safety Level", lambda m: m.safety_level.value.split(" - ")[0]),
        ("Effectiveness", lambda m: f"{m.effectiveness_rating}/10"),
        ("Accessibility", lambda m: m.accessibility.value.split(" - ")[0]),
        ("Cost Range", lambda m: m.cost_range or "Not specified"),
        ("Duration", lambda m: m.typical_duration or "Not specified"),
    ]
    
    for attr_name, attr_func in attributes:
        row = [attr_name]
        for method in methods_to_compare:
            row.append(attr_func(method))
        comparison_table.add_row(*row)
    
    console.print(comparison_table)
    
    # Ask if user wants detailed info
    if Confirm.ask("\nWould you like detailed information about any of these methods?"):
        method_names = {method.name: method.id for method in methods_to_compare}
        method_names_list = list(method_names.keys())
        
        for i, name in enumerate(method_names_list):
            console.print(f"{i+1}. {name}")
        
        choice = Prompt.ask("Select method number for details", 
                          choices=[str(i+1) for i in range(len(method_names_list))])
        selected_name = method_names_list[int(choice)-1]
        selected_id = method_names[selected_name]
        
        console.print("\n" + "="*80 + "\n")
        display_method_detail(selected_id)


@cli.command()
def interactive():
    """Interactive guided exploration of recovery methods."""
    console.print("[bold cyan]Interactive Recovery Method Explorer[/bold cyan]\n")
    
    show_disclaimer()
    
    if not Confirm.ask("Do you understand the medical disclaimer and wish to continue?"):
        console.print("Please consult with healthcare professionals for medical advice.")
        return
    
    console.print("\n[bold]Let's find recovery methods that might be right for your situation.[/bold]")
    console.print("[dim]This is for informational purposes only and does not replace professional medical advice.[/dim]\n")
    
    # Gather preferences
    console.print("[bold]1. What type of approach are you most interested in?[/bold]")
    category_choices = {}
    for i, category in enumerate(MethodCategory, 1):
        category_choices[str(i)] = category
        console.print(f"{i}. {category.value}")
    
    category_choice = Prompt.ask("Select category (or press Enter for all)", 
                               choices=list(category_choices.keys()) + [""], 
                               default="")
    
    selected_category = category_choices.get(category_choice) if category_choice else None
    
    # Evidence level preference
    console.print(f"\n[bold]2. What level of scientific evidence is important to you?[/bold]")
    evidence_choices = {}
    for i, evidence in enumerate(EvidenceLevel, 1):
        evidence_choices[str(i)] = evidence
        console.print(f"{i}. {evidence.value}")
    
    evidence_choice = Prompt.ask("Select minimum evidence level (or press Enter for any)", 
                               choices=list(evidence_choices.keys()) + [""], 
                               default="")
    
    selected_evidence = evidence_choices.get(evidence_choice) if evidence_choice else None
    
    # Safety preference
    console.print(f"\n[bold]3. What is your risk tolerance?[/bold]")
    safety_choices = {}
    for i, safety in enumerate(SafetyLevel, 1):
        safety_choices[str(i)] = safety
        console.print(f"{i}. {safety.value}")
    
    safety_choice = Prompt.ask("Select maximum risk level (or press Enter for any)", 
                             choices=list(safety_choices.keys()) + [""], 
                             default="")
    
    selected_safety = safety_choices.get(safety_choice) if safety_choice else None
    
    # Filter methods based on preferences
    methods = get_all_methods()
    
    if selected_category:
        methods = [m for m in methods if m.category == selected_category]
    
    if selected_evidence:
        # Filter for selected evidence level and above
        evidence_order = list(EvidenceLevel)
        min_evidence_index = evidence_order.index(selected_evidence)
        methods = [m for m in methods if evidence_order.index(m.evidence_level) <= min_evidence_index]
    
    if selected_safety:
        # Filter for selected safety level and safer
        safety_order = [SafetyLevel.SAFE, SafetyLevel.MODERATE_RISK, SafetyLevel.HIGH_RISK, 
                       SafetyLevel.DANGEROUS, SafetyLevel.UNKNOWN]
        max_safety_index = safety_order.index(selected_safety)
        methods = [m for m in methods if safety_order.index(m.safety_level) <= max_safety_index]
    
    # Sort by effectiveness
    methods.sort(key=lambda x: x.effectiveness_rating, reverse=True)
    
    console.print(f"\n[bold]Found {len(methods)} methods matching your preferences:[/bold]\n")
    
    if not methods:
        console.print("[yellow]No methods match all your criteria. Try broadening your preferences.[/yellow]")
        return
    
    # Show top 5 results
    top_methods = methods[:5]
    display_method_summary(top_methods, show_hints=False)
    
    # Offer to show details
    if Confirm.ask(f"\nWould you like detailed information about any of these methods?"):
        method_choices = {str(i+1): method for i, method in enumerate(top_methods)}
        
        for i, method in enumerate(top_methods):
            console.print(f"{i+1}. {method.name}")
        
        choice = Prompt.ask("Select method number", choices=list(method_choices.keys()))
        selected_method = method_choices[choice]
        
        console.print("\n" + "="*80 + "\n")
        display_method_detail(selected_method.id)


# =====================================================
# NEW COMMANDS - Daily Tools
# =====================================================

@cli.command()
@click.argument('method_name')
def quick(method_name):
    """Get quick key facts about a method (e.g., quick naloxone)."""
    info = get_quick_info(method_name)
    
    if not info:
        console.print(f"[red]Method '{method_name}' not found.[/red]")
        console.print("[dim]Try 'python main.py search <term>' to find methods.[/dim]")
        return
    
    console.print(f"\n[bold cyan]⚡ Quick Info: {info['name']}[/bold cyan]\n")
    
    # Key facts in a compact format
    quick_table = Table.grid(padding=1)
    quick_table.add_column(style="bold")
    quick_table.add_column()
    
    quick_table.add_row("📁 Category:", info['category'])
    quick_table.add_row("🛡️ Safety:", info['safety'])
    quick_table.add_row("⭐ Rating:", info['effectiveness'])
    quick_table.add_row("📊 Evidence:", info['evidence'])
    quick_table.add_row("💰 Cost:", info['cost'])
    
    console.print(Panel(quick_table, title="Key Facts", border_style="cyan"))
    
    # Brief description
    console.print(f"\n[bold]What it is:[/bold] {info['what_it_is']}")
    
    if info['key_pros']:
        console.print(f"\n[bold green]Key Benefits:[/bold green]")
        for pro in info['key_pros']:
            console.print(f"  ✓ {pro}")
    
    if info['key_risks']:
        console.print(f"\n[bold red]Key Risks:[/bold red]")
        for risk in info['key_risks']:
            console.print(f"  ⚠️ {risk}")
    
    if info['where_to_find']:
        console.print(f"\n[bold]Where to find:[/bold]")
        for loc in info['where_to_find']:
            console.print(f"  • {loc}")
    
    console.print(f"\n[dim]For full details: python main.py show {method_name}[/dim]")


@cli.command()
def stats():
    """Show database statistics and overview."""
    stats = get_database_stats()
    
    console.print("[bold cyan]📊 Database Statistics[/bold cyan]\n")
    
    # Summary
    summary_table = Table.grid(padding=1)
    summary_table.add_column(style="bold")
    summary_table.add_column(style="green")
    
    summary_table.add_row("Total Recovery Methods:", str(stats['total_methods']))
    summary_table.add_row("Total Resources:", str(stats['total_resources']))
    summary_table.add_row("Crisis Resources:", str(stats['crisis_resources']))
    summary_table.add_row("Categories Covered:", f"{stats['categories_covered']}/8")
    summary_table.add_row("Average Effectiveness:", f"{stats['average_effectiveness']}/10")
    
    console.print(Panel(summary_table, title="Overview", border_style="cyan"))
    
    # Category breakdown
    console.print("\n[bold]Methods by Category:[/bold]")
    cat_table = Table(show_header=True, header_style="bold magenta")
    cat_table.add_column("Category")
    cat_table.add_column("Count", justify="right")
    
    for cat, count in sorted(stats['category_counts'].items(), key=lambda x: x[1], reverse=True):
        cat_table.add_row(cat, str(count))
    
    console.print(cat_table)
    
    # Evidence breakdown
    console.print("\n[bold]Methods by Evidence Level:[/bold]")
    for level, count in stats['evidence_counts'].items():
        bar = "█" * count
        console.print(f"  {level:15} {bar} ({count})")


@cli.command()
@click.argument('sobriety_date')
def sobriety(sobriety_date):
    """Calculate sobriety time from a date (YYYY-MM-DD format)."""
    try:
        result = calculate_sobriety_days(sobriety_date)
    except ValueError as e:
        console.print(f"[red]Error: {e}[/red]")
        console.print("[dim]Use format YYYY-MM-DD (e.g., 2024-01-15)[/dim]")
        return
    
    console.print("\n[bold cyan]🌟 Your Sobriety Journey 🌟[/bold cyan]\n")
    
    # Big number display
    days = result['total_days']
    console.print(f"[bold green]{days}[/bold green] [bold]days of recovery![/bold]")
    console.print()
    
    # Breakdown
    breakdown = Table.grid(padding=1)
    breakdown.add_column(style="bold")
    breakdown.add_column(style="cyan")
    
    breakdown.add_row("That's:", f"{result['weeks']} weeks")
    breakdown.add_row("Or:", f"{result['months']} months")
    if result['years'] > 0:
        breakdown.add_row("Or:", f"{result['years']} year(s) and {days % 365} days")
    
    console.print(Panel(breakdown, border_style="green"))
    
    # Milestone message
    console.print()
    console.print(Panel(result['milestone_message'], title="🎉 Milestone", border_style="yellow"))
    
    console.print("\n[dim]Every day counts. You're doing amazing! 💪[/dim]")


@cli.command()
def motivation():
    """Get a daily motivation quote."""
    quote = get_daily_quote()
    
    console.print()
    console.print(Panel(
        f"[italic cyan]\"{quote}\"[/italic cyan]",
        title="💫 Daily Motivation",
        border_style="cyan",
        padding=(1, 2)
    ))
    console.print()
    console.print("[dim]Remember: Recovery is possible. You are not alone.[/dim]")


@cli.command()
def cope():
    """Get coping strategies for difficult moments."""
    console.print("\n[bold cyan]🧘 Coping Strategies for Difficult Moments[/bold cyan]\n")
    
    strategies = get_multiple_coping_strategies(5)
    
    for i, strategy in enumerate(strategies, 1):
        console.print(Panel(strategy, title=f"Strategy {i}", border_style="green"))
    
    console.print("\n[bold red]🆘 If you're in crisis:[/bold red]")
    console.print("  • Call 988 (Suicide & Crisis Lifeline)")
    console.print("  • Text HOME to 741741")
    console.print("  • Call 911 for medical emergencies")
    
    console.print("\n[dim]Run 'python main.py cope' again for different strategies.[/dim]")


@cli.command()
def checkin():
    """Daily check-in prompts for reflection."""
    console.print("\n[bold cyan]📝 Daily Check-In[/bold cyan]\n")
    
    console.print("Take a moment to reflect on these questions:\n")
    
    prompts = [get_checkin_prompt() for _ in range(3)]
    
    for i, prompt in enumerate(prompts, 1):
        console.print(f"[bold]{i}.[/bold] {prompt}")
        console.print()
    
    console.print("[dim]Consider writing your answers in a journal.[/dim]")
    console.print("[dim]Regular reflection supports long-term recovery.[/dim]")


@cli.command()
def daily():
    """Show all daily recovery tools."""
    console.print("\n[bold cyan]🌅 Daily Recovery Tools[/bold cyan]\n")
    
    # Motivation
    quote = get_daily_quote()
    console.print(Panel(
        f"[italic]\"{quote}\"[/italic]",
        title="💫 Today's Motivation",
        border_style="cyan"
    ))
    
    # Coping strategy
    strategy = get_coping_strategy()
    console.print(Panel(
        strategy,
        title="🧘 Coping Strategy",
        border_style="green"
    ))
    
    # Check-in prompt
    prompt = get_checkin_prompt()
    console.print(Panel(
        prompt,
        title="📝 Reflection Question",
        border_style="yellow"
    ))
    
    console.print("\n[bold]📅 More daily tools:[/bold]")
    console.print("  • [cyan]python main.py motivation[/cyan] - More quotes")
    console.print("  • [cyan]python main.py cope[/cyan] - Coping strategies")
    console.print("  • [cyan]python main.py checkin[/cyan] - Reflection prompts")
    console.print("  • [cyan]python main.py sobriety YYYY-MM-DD[/cyan] - Track your days")


# =====================================================
# EXPORT COMMANDS
# =====================================================

@cli.command()
@click.argument('method_id')
@click.option('--output', '-o', help='Output file path')
def export(method_id, output):
    """Export method information to a text file."""
    try:
        text = export_method_to_text(method_id)
    except ValueError as e:
        console.print(f"[red]Error: {e}[/red]")
        return
    
    if output:
        try:
            with open(output, 'w') as f:
                f.write(text)
            console.print(f"[green]✓ Exported to {output}[/green]")
        except IOError as e:
            console.print(f"[red]Error writing file: {e}[/red]")
    else:
        console.print(text)


@cli.command('crisis-card')
@click.option('--output', '-o', help='Output file path')
def crisis_card(output):
    """Generate a printable crisis resource card."""
    text = export_crisis_card()
    
    if output:
        try:
            with open(output, 'w') as f:
                f.write(text)
            console.print(f"[green]✓ Crisis card exported to {output}[/green]")
            console.print("[dim]Print this card and keep it accessible.[/dim]")
        except IOError as e:
            console.print(f"[red]Error writing file: {e}[/red]")
    else:
        console.print(text)
        console.print("\n[dim]Use --output <file> to save to a file for printing.[/dim]")


# =====================================================
# MAIN ENTRY
# =====================================================

if __name__ == '__main__':
    # Show disclaimer on startup
    if len(sys.argv) == 1:  # No arguments provided
        show_disclaimer()
        console.print("[bold]🆘 If you're in crisis: Call 988 or text HOME to 741741[/bold]\n")
        console.print("[bold]Available commands:[/bold]")
        console.print("  • [cyan]python main.py list[/cyan] - List all recovery methods")
        console.print("  • [cyan]python main.py search <term>[/cyan] - Search methods")
        console.print("  • [cyan]python main.py show <id>[/cyan] - Show method details")
        console.print("  • [cyan]python main.py quick <id>[/cyan] - Quick key facts")
        console.print("  • [cyan]python main.py interactive[/cyan] - Guided exploration")
        console.print("  • [cyan]python main.py daily[/cyan] - Daily recovery tools")
        console.print("  • [cyan]python main.py emergency[/cyan] - Crisis resources")
        console.print("  • [cyan]python main.py stats[/cyan] - Database overview")
        console.print("\n[bold]Use 'python main.py --help' for all commands.[/bold]\n")
    
    cli()