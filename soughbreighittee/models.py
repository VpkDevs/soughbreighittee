"""
Data models for the Soughbreighittee recovery app.
"""

from datetime import datetime
from typing import List, Dict, Optional, Literal
from pydantic import BaseModel, Field
from enum import Enum


class MethodCategory(str, Enum):
    """Categories of recovery methods."""
    MEDICAL_ASSISTED_TREATMENT = "Medical-Assisted Treatment (MAT)"
    BEHAVIORAL_THERAPY = "Behavioral Therapy"
    SUPPORT_GROUPS = "Support Groups"
    ALTERNATIVE_COMPLEMENTARY = "Alternative/Complementary"
    HARM_REDUCTION = "Harm Reduction"
    CRISIS_EMERGENCY = "Crisis/Emergency"
    HOLISTIC_WELLNESS = "Holistic Wellness"
    PEER_SUPPORT = "Peer Support"


class EvidenceLevel(str, Enum):
    """Evidence levels for treatment effectiveness."""
    HIGH = "High - Strong scientific evidence"
    MODERATE = "Moderate - Some scientific evidence"
    LIMITED = "Limited - Minimal scientific evidence"
    ANECDOTAL = "Anecdotal - Personal reports only"
    EXPERIMENTAL = "Experimental - Under research"
    CONTROVERSIAL = "Controversial - Mixed or disputed evidence"


class SafetyLevel(str, Enum):
    """Safety levels for different methods."""
    SAFE = "Safe - Generally considered safe when used properly"
    MODERATE_RISK = "Moderate Risk - Some potential risks or side effects"
    HIGH_RISK = "High Risk - Significant risks or potential dangers"
    DANGEROUS = "Dangerous - Known to be harmful or potentially fatal"
    UNKNOWN = "Unknown - Safety profile not well established"


class AccessibilityLevel(str, Enum):
    """Accessibility levels for different methods."""
    HIGH = "High - Widely available and accessible"
    MODERATE = "Moderate - Available with some barriers"
    LIMITED = "Limited - Restricted availability"
    PRESCRIPTION_ONLY = "Prescription Only - Requires medical prescription"
    SPECIALIZED_CARE = "Specialized Care - Requires specialized facilities"


class RecoveryMethod(BaseModel):
    """Model representing a recovery method for opiate addiction."""
    
    id: str = Field(..., description="Unique identifier for the method")
    name: str = Field(..., description="Name of the recovery method")
    category: MethodCategory = Field(..., description="Category this method belongs to")
    
    # Core information
    description: str = Field(..., description="Detailed description of the method")
    how_it_works: str = Field(..., description="Explanation of how the method works")
    typical_duration: Optional[str] = Field(None, description="Typical duration of treatment")
    
    # Evidence and effectiveness
    evidence_level: EvidenceLevel = Field(..., description="Level of scientific evidence")
    effectiveness_rating: int = Field(..., ge=1, le=10, description="Effectiveness rating 1-10")
    success_rate: Optional[str] = Field(None, description="Success rate information if available")
    
    # Safety and risks
    safety_level: SafetyLevel = Field(..., description="Safety level assessment")
    risks_side_effects: List[str] = Field(default_factory=list, description="Known risks and side effects")
    contraindications: List[str] = Field(default_factory=list, description="When this method should not be used")
    
    # Practical information
    accessibility: AccessibilityLevel = Field(..., description="How accessible this method is")
    cost_range: Optional[str] = Field(None, description="Typical cost range")
    insurance_coverage: Optional[str] = Field(None, description="Insurance coverage information")
    
    # Requirements and logistics
    requirements: List[str] = Field(default_factory=list, description="Requirements to use this method")
    where_to_find: List[str] = Field(default_factory=list, description="Where to access this method")
    
    # Combination and interaction information
    can_combine_with: List[str] = Field(default_factory=list, description="Methods that can be combined with this")
    cannot_combine_with: List[str] = Field(default_factory=list, description="Methods that should not be combined")
    
    # Additional details
    pros: List[str] = Field(default_factory=list, description="Advantages of this method")
    cons: List[str] = Field(default_factory=list, description="Disadvantages of this method")
    best_for: List[str] = Field(default_factory=list, description="Who this method works best for")
    not_recommended_for: List[str] = Field(default_factory=list, description="Who should avoid this method")
    
    # Resources
    resources: List[str] = Field(default_factory=list, description="Additional resources and links")
    
    # Metadata
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    

class UserProgress(BaseModel):
    """Model for tracking user progress and preferences."""
    
    user_id: str = Field(..., description="User identifier")
    current_methods: List[str] = Field(default_factory=list, description="Currently using methods")
    tried_methods: List[str] = Field(default_factory=list, description="Previously tried methods")
    interested_methods: List[str] = Field(default_factory=list, description="Methods interested in trying")
    
    # Progress tracking
    sobriety_date: Optional[datetime] = Field(None, description="Date of sobriety start")
    recovery_goals: List[str] = Field(default_factory=list, description="Personal recovery goals")
    
    # Preferences
    preferred_categories: List[MethodCategory] = Field(default_factory=list)
    risk_tolerance: Optional[SafetyLevel] = Field(None, description="User's risk tolerance")
    budget_range: Optional[str] = Field(None, description="Budget constraints")
    
    # Metadata
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)


class Resource(BaseModel):
    """Model for additional resources and information."""
    
    id: str = Field(..., description="Unique identifier")
    title: str = Field(..., description="Resource title")
    type: Literal["website", "phone", "app", "book", "organization"] = Field(..., description="Type of resource")
    description: str = Field(..., description="Description of the resource")
    url: Optional[str] = Field(None, description="URL if applicable")
    phone: Optional[str] = Field(None, description="Phone number if applicable")
    category: MethodCategory = Field(..., description="Category this resource relates to")
    is_crisis_resource: bool = Field(False, description="Whether this is a crisis resource")
    is_free: bool = Field(True, description="Whether this resource is free")
    
    created_at: datetime = Field(default_factory=datetime.now)