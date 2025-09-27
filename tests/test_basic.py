"""
Basic tests for the Soughbreighittee application.
"""

import sys
import os
# Add the parent directory to the path so we can import the package
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from soughbreighittee.models import RecoveryMethod, MethodCategory, EvidenceLevel, SafetyLevel
from soughbreighittee.database import get_all_methods, get_methods_by_category, search_methods, get_crisis_resources


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
    
    # Search for non-existent method
    results = search_methods("nonexistentmethod12345")
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
    
    # Naloxone should be safe
    naloxone_methods = [m for m in methods if "naloxone" in m.name.lower()]
    assert len(naloxone_methods) > 0
    for method in naloxone_methods:
        assert method.safety_level == SafetyLevel.SAFE


def test_evidence_levels_present():
    """Test that various evidence levels are represented."""
    methods = get_all_methods()
    evidence_levels = {method.evidence_level for method in methods}
    
    # Should have high evidence methods (like FDA approved MAT)
    assert EvidenceLevel.HIGH in evidence_levels


if __name__ == "__main__":
    # Simple test runner if pytest is not available
    test_functions = [
        test_get_all_methods,
        test_get_methods_by_category,
        test_search_methods,
        test_crisis_resources,
        test_method_data_integrity,
        test_specific_high_priority_methods,
        test_safety_levels_appropriate,
        test_evidence_levels_present
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