#!/usr/bin/env python3
"""
Soughbreighittee - Comprehensive Harm Reduction and Addiction Recovery App

Main command-line interface for exploring recovery methods for Opiate Use Disorder.
"""

import sys
from typing import List
import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.markdown import Markdown
from rich.text import Text
from rich.prompt import Prompt, Confirm

from . import __version__, EMERGENCY_CONTACTS, DISCLAIMER
from .models import MethodCategory, EvidenceLevel, SafetyLevel, AccessibilityLevel
from .database import (
    get_all_methods, get_methods_by_category, get_method_by_id,
    search_methods, get_crisis_resources
)

console = Console()

# Constants
MIN_EFFECTIVENESS_RATING = 1
MAX_EFFECTIVENESS_RATING = 10
EFFECTIVENESS_THRESHOLD_HIGH = 7
EFFECTIVENESS_THRESHOLD_MEDIUM = 5
MAX_COMPARE_METHODS = 5


def show_disclaimer() -> None:
    """Display the medical disclaimer."""
    disclaimer_panel = Panel(
        DISCLAIMER,
        title="[bold red]MEDICAL DISCLAIMER[/bold red]",
        border_style="red"
    )
    console.print(disclaimer_panel)
    console.print()


def show_emergency_contacts() -> None:
    """Display emergency contacts."""
    emergency_text = "\n".join([
        f"• {name}: [bold]{contact}[/bold]"
        for name, contact in EMERGENCY_CONTACTS.items()
    ])
    
    emergency_panel = Panel(
        emergency_text,
        title="[bold red]EMERGENCY CONTACTS[/bold red]",
        border_style="red"
    )
    console.print(emergency_panel)
    console.print()


def display_method_summary(methods: List) -> None:
    """Display a table summary of methods."""
    if not methods:
        console.print("[yellow]No methods found matching your criteria.[/yellow]")
        console.print("[dim]Try adjusting your filters or use 'list' without filters to see all methods.[/dim]")
        return

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Name", style="cyan")
    table.add_column("Category", style="green")
    table.add_column("Evidence Level", style="blue")
    table.add_column("Safety", style="yellow")
    table.add_column("Effectiveness", style="red")
    table.add_column("Accessibility", style="white")

    for method in methods:
        # Color code effectiveness rating
        effectiveness_color = "green" if method.effectiveness_rating >= EFFECTIVENESS_THRESHOLD_HIGH else "yellow" if method.effectiveness_rating >= EFFECTIVENESS_THRESHOLD_MEDIUM else "red"
        effectiveness = f"[{effectiveness_color}]{method.effectiveness_rating}/{MAX_EFFECTIVENESS_RATING}[/{effectiveness_color}]"
        
        table.add_row(
            method.name,
            method.category.value,
            method.evidence_level.value.split(" - ")[0],  # Just the level, not description
            method.safety_level.value.split(" - ")[0],    # Just the level, not description
            effectiveness,
            method.accessibility.value.split(" - ")[0]    # Just the level, not description
        )

    console.print(table)


def display_method_detail(method_id: str) -> None:
    """Display detailed information about a specific method."""
    try:
        method = get_method_by_id(method_id)
    except ValueError as e:
        console.print(f"[red]Error: {e}[/red]")
        return

    # Main method information
    console.print(f"\n[bold cyan]{method.name}[/bold cyan]")
    console.print(f"[dim]Category: {method.category.value}[/dim]\n")
    
    # Description
    console.print(Panel(method.description, title="Description"))
    
    # How it works
    console.print(Panel(method.how_it_works, title="How It Works"))
    
    # Key metrics table
    metrics_table = Table.grid(padding=1)
    metrics_table.add_column(style="bold")
    metrics_table.add_column()
    
    metrics_table.add_row("Evidence Level:", f"[blue]{method.evidence_level.value}[/blue]")
    metrics_table.add_row("Safety Level:", f"[yellow]{method.safety_level.value}[/yellow]")
    metrics_table.add_row("Effectiveness Rating:", f"[red]{method.effectiveness_rating}/{MAX_EFFECTIVENESS_RATING}[/red]")
    metrics_table.add_row("Accessibility:", f"[green]{method.accessibility.value}[/green]")
    
    if method.typical_duration:
        metrics_table.add_row("Typical Duration:", method.typical_duration)
    if method.cost_range:
        metrics_table.add_row("Cost Range:", method.cost_range)
    if method.insurance_coverage:
        metrics_table.add_row("Insurance Coverage:", method.insurance_coverage)
    if method.success_rate:
        metrics_table.add_row("Success Rate:", method.success_rate)
    
    console.print(Panel(metrics_table, title="Key Information"))
    
    # Pros and Cons
    if method.pros or method.cons:
        pros_cons_table = Table.grid(padding=2)
        pros_cons_table.add_column("Pros", style="green")
        pros_cons_table.add_column("Cons", style="red")
        
        pros_text = "\n".join([f"✓ {pro}" for pro in method.pros]) if method.pros else ""
        cons_text = "\n".join([f"✗ {con}" for con in method.cons]) if method.cons else ""
        
        pros_cons_table.add_row(pros_text, cons_text)
        console.print(Panel(pros_cons_table, title="Pros and Cons"))
    
    # Safety information
    if method.risks_side_effects or method.contraindications:
        safety_content = ""
        if method.risks_side_effects:
            safety_content += "[bold]Risks and Side Effects:[/bold]\n"
            safety_content += "\n".join([f"• {risk}" for risk in method.risks_side_effects])
            safety_content += "\n\n"
        
        if method.contraindications:
            safety_content += "[bold]Contraindications (when NOT to use):[/bold]\n"
            safety_content += "\n".join([f"• {contra}" for contra in method.contraindications])
        
        console.print(Panel(safety_content, title="[red]Safety Information[/red]", border_style="red"))
    
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
        
        console.print(Panel(suitability_content, title="Suitability"))
    
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
        
        console.print(Panel(combo_content, title="Combination Information"))
    
    # Resources
    if method.resources:
        resources_content = "\n".join([f"• {resource}" for resource in method.resources])
        console.print(Panel(resources_content, title="Additional Resources"))


@click.group()
@click.version_option(__version__)
def cli():
    """
    Soughbreighittee - Comprehensive Harm Reduction and Addiction Recovery App
    
    A comprehensive tool for exploring recovery methods for Opiate Use Disorder.
    Get detailed information about all known recovery approaches, from evidence-based
    medical treatments to alternative and harm reduction strategies.
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
        console.print("[bold]Crisis Resources:[/bold]\n")
        for resource in crisis_resources:
            resource_text = f"[bold cyan]{resource.title}[/bold cyan]\n"
            resource_text += f"{resource.description}\n"
            if resource.phone:
                resource_text += f"[bold]Contact: {resource.phone}[/bold]"
            console.print(Panel(resource_text))


@cli.command()
@click.option('--category', type=click.Choice([cat.name for cat in MethodCategory]), 
              help='Filter by category')
@click.option('--evidence', type=click.Choice([ev.name for ev in EvidenceLevel]),
              help='Filter by evidence level')
@click.option('--safety', type=click.Choice([sf.name for sf in SafetyLevel]),
              help='Filter by safety level')
@click.option('--accessibility', type=click.Choice([ac.name for ac in AccessibilityLevel]),
              help='Filter by accessibility')
@click.option('--min-effectiveness', type=click.IntRange(MIN_EFFECTIVENESS_RATING, MAX_EFFECTIVENESS_RATING), 
              help=f'Minimum effectiveness rating ({MIN_EFFECTIVENESS_RATING}-{MAX_EFFECTIVENESS_RATING})')
def list(category, evidence, safety, accessibility, min_effectiveness):
    """List all available recovery methods with optional filters.
    
    Examples:
      soughbreighittee list
      soughbreighittee list --category MEDICAL_ASSISTED_TREATMENT
      soughbreighittee list --evidence HIGH --min-effectiveness 7
      soughbreighittee list --safety SAFE
    """
    
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
    """Show detailed information about a specific method.
    
    Examples:
      soughbreighittee show methadone
      soughbreighittee show naloxone
      soughbreighittee show buprenorphine
    """
    display_method_detail(method_id)


@cli.command()
@click.argument('query')
def search(query):
    """Search for recovery methods by keyword.
    
    Examples:
      soughbreighittee search methadone
      soughbreighittee search therapy
      soughbreighittee search "harm reduction"
    """
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
    
    while len(methods_to_compare) < MAX_COMPARE_METHODS:  # Limit for readability
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
    display_method_summary(top_methods)
    
    # Offer to show details
    if Confirm.ask(f"\nWould you like detailed information about any of these methods?"):
        method_choices = {str(i+1): method for i, method in enumerate(top_methods)}
        
        for i, method in enumerate(top_methods):
            console.print(f"{i+1}. {method.name}")
        
        choice = Prompt.ask("Select method number", choices=list(method_choices.keys()))
        selected_method = method_choices[choice]
        
        console.print("\n" + "="*80 + "\n")
        display_method_detail(selected_method.id)


if __name__ == '__main__':
    # Show disclaimer on startup
    if len(sys.argv) == 1:  # No arguments provided
        show_disclaimer()
        console.print("[bold]Use 'soughbreighittee --help' to see available commands.[/bold]")
        console.print("[bold]Use 'soughbreighittee interactive' for guided exploration.[/bold]\n")
    
    cli()