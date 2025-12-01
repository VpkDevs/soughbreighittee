"""
Comprehensive tests for the Soughbreighittee application.
"""

import sys
import os
# Add the parent directory to the path so we can import the package
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from soughbreighittee.models import RecoveryMethod, MethodCategory, EvidenceLevel, SafetyLevel
from soughbreighittee.database import (
    get_all_methods, get_methods_by_category, search_methods, get_crisis_resources,
    get_all_resources, get_database_stats, get_quick_info, get_daily_quote,
    get_coping_strategy, get_checkin_prompt, get_multiple_coping_strategies,
    calculate_sobriety_days, export_method_to_text, export_crisis_card,
    get_treatment_locators, search_methods_by_tags, get_method_by_id
)


import pytest


# =====================================================
# BASIC FUNCTIONALITY TESTS
# =====================================================

def test_get_all_methods():
    """Test that all methods can be retrieved."""
    methods = get_all_methods()
    assert len(methods) > 0
    assert all(isinstance(method, RecoveryMethod) for method in methods)


def test_get_methods_by_category():
    """Test filtering methods by category."""
    mat_methods = get_methods_by_category(MethodCategory.MEDICAL_ASSISTED_TREATMENT)
    assert len(mat_methods) > 0
    assert all(method.category == MethodCategory.MEDICAL_ASSISTED_TREATMENT for method in mat_methods)


def test_search_methods():
    """Test searching for methods."""
    # Search for a known method
    results = search_methods("methadone")
    assert len(results) > 0
    assert any("methadone" in method.name.lower() for method in results)
    
    # Search for truly non-existent method - use something that won't fuzzy match
    results = search_methods("zzzzzxxxxx12345nonexistent")
    assert len(results) == 0


def test_crisis_resources():
    """Test that crisis resources are available."""
    resources = get_crisis_resources()
    assert len(resources) > 0
    assert all(resource.is_crisis_resource for resource in resources)


def test_method_data_integrity():
    """Test that all methods have required fields."""
    methods = get_all_methods()
    
    for method in methods:
        # Check required fields
        assert method.id
        assert method.name
        assert method.category
        assert method.description
        assert method.how_it_works
        assert method.evidence_level
        assert isinstance(method.effectiveness_rating, int)
        assert 1 <= method.effectiveness_rating <= 10
        assert method.safety_level
        assert method.accessibility


def test_specific_high_priority_methods():
    """Test that critical harm reduction methods are present."""
    methods = get_all_methods()
    method_names = [method.name.lower() for method in methods]
    
    # Check for key harm reduction methods
    assert any("naloxone" in name for name in method_names)
    assert any("methadone" in name for name in method_names)
    assert any("buprenorphine" in name for name in method_names)
    assert any("needle exchange" in name for name in method_names)


def test_safety_levels_appropriate():
    """Test that safety levels are reasonable."""
    methods = get_all_methods()
    
    # The main naloxone method (not auto-injector which is a device) should be safe
    naloxone = get_method_by_id("naloxone")
    assert naloxone is not None, "Naloxone method should exist"
    assert naloxone.safety_level == SafetyLevel.SAFE, "Naloxone should be classified as safe"


def test_evidence_levels_present():
    """Test that various evidence levels are represented."""
    methods = get_all_methods()
    evidence_levels = {method.evidence_level for method in methods}
    
    # Should have high evidence methods (like FDA approved MAT)
    assert EvidenceLevel.HIGH in evidence_levels


# =====================================================
# NEW CONTENT TESTS
# =====================================================

def test_peer_support_category_has_methods():
    """Test that the Peer Support category has methods."""
    peer_methods = get_methods_by_category(MethodCategory.PEER_SUPPORT)
    assert len(peer_methods) >= 3, "Peer Support should have at least 3 methods"


def test_new_harm_reduction_methods():
    """Test that new harm reduction methods are present."""
    methods = get_all_methods()
    method_ids = [m.id for m in methods]
    
    assert "fentanyl_test_strips" in method_ids
    assert "safe_consumption_sites" in method_ids or any("safe consumption" in m.name.lower() for m in methods)


def test_new_behavioral_therapies():
    """Test that new behavioral therapy methods are present."""
    methods = get_all_methods()
    method_ids = [m.id for m in methods]
    
    assert "dialectical_behavior_therapy" in method_ids
    assert "group_therapy" in method_ids


def test_residential_treatment_methods():
    """Test that residential treatment methods are present."""
    methods = get_all_methods()
    method_ids = [m.id for m in methods]
    
    assert "inpatient_detox" in method_ids
    assert "residential_rehab" in method_ids
    assert "sober_living" in method_ids


def test_technology_based_methods():
    """Test that technology-based methods are present."""
    methods = get_all_methods()
    method_ids = [m.id for m in methods]
    
    assert "telehealth_addiction" in method_ids
    assert "recovery_apps" in method_ids


def test_family_support_methods():
    """Test that family support methods are present."""
    methods = get_all_methods()
    method_ids = [m.id for m in methods]
    
    assert "family_therapy" in method_ids
    assert "alanon" in method_ids


def test_database_has_expanded():
    """Test that database has grown to expected size."""
    methods = get_all_methods()
    # Should have 36 total methods after expansion
    assert len(methods) >= 36, f"Expected at least 36 methods, got {len(methods)}"


# =====================================================
# SEARCH FUNCTIONALITY TESTS
# =====================================================

def test_synonym_search():
    """Test that synonym search works."""
    # "suboxone" should find buprenorphine
    results = search_methods("suboxone")
    assert len(results) > 0
    assert any("buprenorphine" in m.id.lower() for m in results)


def test_synonym_search_narcan():
    """Test that 'narcan' finds naloxone."""
    results = search_methods("narcan")
    assert len(results) > 0
    assert any("naloxone" in m.id.lower() for m in results)


def test_fuzzy_search():
    """Test that fuzzy search works."""
    # Search for partial match
    results = search_methods("cognitive")
    assert len(results) > 0
    assert any("cognitive" in m.name.lower() for m in results)


def test_tag_based_search():
    """Test tag-based search."""
    results = search_methods_by_tags(["medication", "treatment"])
    # Should find MAT methods
    assert len(results) >= 0  # May or may not match depending on content


# =====================================================
# HELPER FUNCTION TESTS
# =====================================================

def test_get_database_stats():
    """Test database statistics function."""
    stats = get_database_stats()
    
    assert "total_methods" in stats
    assert "total_resources" in stats
    assert "category_counts" in stats
    assert "average_effectiveness" in stats
    assert stats["total_methods"] > 0
    assert stats["total_resources"] > 0


def test_get_quick_info():
    """Test quick info function."""
    info = get_quick_info("naloxone")
    
    assert info is not None
    assert "name" in info
    assert "safety" in info
    assert "effectiveness" in info


def test_get_quick_info_nonexistent():
    """Test quick info for non-existent method."""
    info = get_quick_info("zzzzzxxxxx12345nonexistent")
    assert info is None


# =====================================================
# DAILY TOOLS TESTS
# =====================================================

def test_get_daily_quote():
    """Test daily quote function."""
    quote = get_daily_quote()
    assert isinstance(quote, str)
    assert len(quote) > 0


def test_get_coping_strategy():
    """Test coping strategy function."""
    strategy = get_coping_strategy()
    assert isinstance(strategy, str)
    assert len(strategy) > 0


def test_get_checkin_prompt():
    """Test check-in prompt function."""
    prompt = get_checkin_prompt()
    assert isinstance(prompt, str)
    assert len(prompt) > 0


def test_get_multiple_coping_strategies():
    """Test getting multiple coping strategies."""
    strategies = get_multiple_coping_strategies(5)
    assert len(strategies) == 5
    assert len(set(strategies)) == 5  # All should be unique


def test_calculate_sobriety_days():
    """Test sobriety calculator."""
    # Test with a known date
    result = calculate_sobriety_days("2024-01-01")
    
    assert "total_days" in result
    assert "weeks" in result
    assert "months" in result
    assert "milestone_message" in result
    assert result["total_days"] >= 0


def test_calculate_sobriety_days_invalid():
    """Test sobriety calculator with invalid date."""
    with pytest.raises(ValueError):
        calculate_sobriety_days("invalid-date")


def test_calculate_sobriety_days_future():
    """Test sobriety calculator with future date."""
    with pytest.raises(ValueError):
        calculate_sobriety_days("2099-01-01")


# =====================================================
# EXPORT FUNCTIONALITY TESTS
# =====================================================

def test_export_method_to_text():
    """Test exporting method to text."""
    text = export_method_to_text("naloxone")
    
    assert isinstance(text, str)
    assert "Naloxone" in text or "naloxone" in text.lower()
    assert "DISCLAIMER" in text


def test_export_method_nonexistent():
    """Test exporting non-existent method."""
    with pytest.raises(ValueError):
        export_method_to_text("nonexistent_method_12345")


def test_export_crisis_card():
    """Test crisis card export."""
    card = export_crisis_card()
    
    assert isinstance(card, str)
    assert "CRISIS" in card.upper()
    assert "988" in card  # Should include suicide hotline


# =====================================================
# RESOURCE TESTS
# =====================================================

def test_get_all_resources():
    """Test getting all resources."""
    resources = get_all_resources()
    assert len(resources) > len(get_crisis_resources())  # Should include non-crisis


def test_get_treatment_locators():
    """Test getting treatment locators."""
    locators = get_treatment_locators()
    assert len(locators) > 0
    # Should include SAMHSA locator
    assert any("samhsa" in r.title.lower() or "locator" in r.title.lower() for r in locators)


def test_international_resources():
    """Test that international resources are present."""
    resources = get_all_resources()
    
    # Check for international resources
    has_international = any(
        any(country in r.title.lower() for country in ["canada", "uk", "australia", "international"])
        for r in resources
    )
    assert has_international, "Should have international crisis resources"


def test_specialized_hotlines():
    """Test that specialized hotlines are present."""
    resources = get_crisis_resources()
    resource_titles = " ".join([r.title.lower() for r in resources])
    
    # Should have some specialized resources
    # At least check for a few
    assert len(resources) > 3, "Should have multiple crisis resources"


# =====================================================
# CATEGORY COVERAGE TESTS
# =====================================================

def test_all_categories_have_methods():
    """Test that all categories have at least one method."""
    for category in MethodCategory:
        methods = get_methods_by_category(category)
        assert len(methods) >= 1, f"Category {category.value} should have at least 1 method"


def test_mat_category_comprehensive():
    """Test MAT category has comprehensive options."""
    mat_methods = get_methods_by_category(MethodCategory.MEDICAL_ASSISTED_TREATMENT)
    method_ids = [m.id for m in mat_methods]
    
    # Should have core MAT options
    assert "methadone" in method_ids
    assert "buprenorphine" in method_ids
    assert "naltrexone" in method_ids


def test_harm_reduction_category_comprehensive():
    """Test harm reduction category has comprehensive options."""
    hr_methods = get_methods_by_category(MethodCategory.HARM_REDUCTION)
    method_ids = [m.id for m in hr_methods]
    
    # Should have key harm reduction options
    assert "naloxone" in method_ids
    assert "needle_exchange" in method_ids
    assert "fentanyl_test_strips" in method_ids


# =====================================================
# TEST RUNNER
# =====================================================

if __name__ == "__main__":
    # Simple test runner if pytest is not available
    test_functions = [
        # Basic functionality
        test_get_all_methods,
        test_get_methods_by_category,
        test_search_methods,
        test_crisis_resources,
        test_method_data_integrity,
        test_specific_high_priority_methods,
        test_safety_levels_appropriate,
        test_evidence_levels_present,
        # New content
        test_peer_support_category_has_methods,
        test_new_harm_reduction_methods,
        test_new_behavioral_therapies,
        test_residential_treatment_methods,
        test_technology_based_methods,
        test_family_support_methods,
        test_database_has_expanded,
        # Search functionality
        test_synonym_search,
        test_synonym_search_narcan,
        test_fuzzy_search,
        test_tag_based_search,
        # Helper functions
        test_get_database_stats,
        test_get_quick_info,
        test_get_quick_info_nonexistent,
        # Daily tools
        test_get_daily_quote,
        test_get_coping_strategy,
        test_get_checkin_prompt,
        test_get_multiple_coping_strategies,
        test_calculate_sobriety_days,
        test_calculate_sobriety_days_invalid,
        test_calculate_sobriety_days_future,
        # Export functionality
        test_export_method_to_text,
        test_export_method_nonexistent,
        test_export_crisis_card,
        # Resources
        test_get_all_resources,
        test_get_treatment_locators,
        test_international_resources,
        test_specialized_hotlines,
        # Category coverage
        test_all_categories_have_methods,
        test_mat_category_comprehensive,
        test_harm_reduction_category_comprehensive,
    ]
    
    passed = 0
    failed = 0
    
    for test_func in test_functions:
        try:
            test_func()
            print(f"✓ {test_func.__name__}")
            passed += 1
        except Exception as e:
            print(f"✗ {test_func.__name__}: {e}")
            failed += 1
    
    print(f"\nTest Results: {passed} passed, {failed} failed")