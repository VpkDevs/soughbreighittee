"""
Database of recovery methods for opiate addiction.

This module contains a comprehensive collection of all known recovery methods
for Opiate Use Disorder, including both evidence-based and alternative approaches.
"""

import random
from datetime import datetime, date
from typing import Dict, List, Optional

from dateutil.relativedelta import relativedelta

from .models import RecoveryMethod, MethodCategory, EvidenceLevel, SafetyLevel, AccessibilityLevel, Resource

# Synonym mapping for better search
SEARCH_SYNONYMS: Dict[str, List[str]] = {
    "buprenorphine": ["suboxone", "subutex", "sublocade", "bupe"],
    "methadone": ["dolophine", "methadose"],
    "naltrexone": ["vivitrol", "revia"],
    "naloxone": ["narcan", "evzio", "kloxxado"],
    "cognitive_behavioral_therapy": ["cbt", "cognitive therapy", "behavioral therapy"],
    "dialectical_behavior_therapy": ["dbt"],
    "motivational_interviewing": ["mi", "motivational enhancement"],
    "motivational_enhancement_therapy": ["met"],
    "narcotics_anonymous": ["na", "12 step", "twelve step"],
    "smart_recovery": ["smart"],
    "needle_exchange": ["syringe exchange", "ssp", "needle program", "harm reduction"],
    "fentanyl_test_strips": ["fts", "fentanyl testing", "test strips"],
    "recovery_coaching": ["recovery coach", "peer coach"],
    "peer_support_specialist": ["peer specialist", "peer support", "peer mentor"],
    "telehealth_addiction": ["telemedicine", "online addiction treatment", "virtual treatment"],
}


# Comprehensive database of recovery methods
RECOVERY_METHODS_DB: Dict[str, RecoveryMethod] = {
    
    # Medical-Assisted Treatment (MAT)
    "methadone": RecoveryMethod(
        id="methadone",
        name="Methadone Maintenance Treatment",
        category=MethodCategory.MEDICAL_ASSISTED_TREATMENT,
        description="Long-acting opioid agonist medication used to treat opioid dependence by reducing cravings and withdrawal symptoms without producing euphoria.",
        how_it_works="Methadone binds to opioid receptors in the brain, preventing withdrawal and reducing cravings while blocking the effects of other opioids.",
        typical_duration="Months to years, often long-term maintenance",
        evidence_level=EvidenceLevel.HIGH,
        effectiveness_rating=8,
        success_rate="60-90% retention rates in treatment programs",
        safety_level=SafetyLevel.MODERATE_RISK,
        risks_side_effects=[
            "Respiratory depression (especially when combined with other depressants)",
            "Constipation", "Drowsiness", "Nausea", "Sweating", "Weight gain",
            "Potential for dependence", "QT prolongation (heart rhythm)"
        ],
        contraindications=[
            "Severe respiratory depression", "Acute bronchial asthma",
            "Known hypersensitivity", "Concurrent MAO inhibitor use"
        ],
        accessibility=AccessibilityLevel.SPECIALIZED_CARE,
        cost_range="$4,000-$13,000 per year",
        insurance_coverage="Often covered by Medicaid and many insurance plans",
        requirements=[
            "Medical evaluation", "Documented opioid dependence",
            "Daily clinic visits initially", "Regular drug testing",
            "Counseling participation"
        ],
        where_to_find=[
            "Licensed methadone clinics", "Opioid treatment programs (OTP)",
            "SAMHSA treatment locator"
        ],
        can_combine_with=["Counseling", "Support groups", "Behavioral therapy"],
        cannot_combine_with=["Naltrexone", "Other opioid antagonists"],
        pros=[
            "Reduces opioid cravings", "Prevents withdrawal symptoms",
            "Allows normal daily functioning", "Reduces overdose risk",
            "Long treatment history", "Can be used during pregnancy"
        ],
        cons=[
            "Daily clinic visits required", "Potential for dependence",
            "Social stigma", "Side effects", "Requires long-term commitment"
        ],
        best_for=[
            "Individuals with long-term opioid dependence",
            "Those who have failed other treatments",
            "Pregnant women with OUD"
        ],
        not_recommended_for=[
            "Those seeking complete abstinence immediately",
            "People with severe heart conditions",
            "Those unable to attend daily visits"
        ],
        resources=[
            "SAMHSA OTP Directory",
            "American Association for the Treatment of Opioid Dependence"
        ]
    ),

    "buprenorphine": RecoveryMethod(
        id="buprenorphine",
        name="Buprenorphine (Suboxone, Subutex)",
        category=MethodCategory.MEDICAL_ASSISTED_TREATMENT,
        description="Partial opioid agonist medication that reduces cravings and withdrawal symptoms with lower risk of overdose compared to full agonists.",
        how_it_works="Partial agonist activity at opioid receptors provides enough activation to prevent withdrawal while having a 'ceiling effect' that reduces overdose risk.",
        typical_duration="Months to years, can be tapered gradually",
        evidence_level=EvidenceLevel.HIGH,
        effectiveness_rating=8,
        success_rate="40-60% at 6 months, higher with longer treatment",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=[
            "Constipation", "Nausea", "Vomiting", "Headache",
            "Dizziness", "Drowsiness", "Insomnia", "Sweating"
        ],
        contraindications=[
            "Severe respiratory depression", "Acute or severe bronchial asthma",
            "Known hypersensitivity", "Concurrent benzodiazepine use (caution)"
        ],
        accessibility=AccessibilityLevel.PRESCRIPTION_ONLY,
        cost_range="$100-$400 per month",
        insurance_coverage="Widely covered by insurance plans",
        requirements=[
            "Prescription from certified physician",
            "Regular medical monitoring", "Drug testing",
            "Counseling recommended"
        ],
        where_to_find=[
            "Certified physicians", "Addiction treatment centers",
            "Primary care providers", "SAMHSA provider locator"
        ],
        can_combine_with=[
            "Counseling", "Support groups", "Behavioral therapy",
            "Most other medications (with medical supervision)"
        ],
        cannot_combine_with=["Naltrexone", "Full opioid agonists"],
        pros=[
            "Lower overdose risk", "Can be prescribed in office settings",
            "Flexible dosing", "Good safety profile",
            "Allows normal functioning", "Can be taken home"
        ],
        cons=[
            "Can be diverted/abused", "Precipitated withdrawal if used too soon",
            "Requires certified prescriber", "Can cause dependence"
        ],
        best_for=[
            "Individuals seeking outpatient treatment",
            "Those with less severe addiction",
            "People who need flexibility in treatment"
        ],
        not_recommended_for=[
            "Those with severe liver disease",
            "People actively using benzodiazepines",
            "Those seeking immediate complete abstinence"
        ],
        resources=[
            "SAMHSA Buprenorphine Locator",
            "American Society of Addiction Medicine"
        ]
    ),

    "naltrexone": RecoveryMethod(
        id="naltrexone",
        name="Naltrexone (Vivitrol)",
        category=MethodCategory.MEDICAL_ASSISTED_TREATMENT,
        description="Opioid antagonist that blocks the effects of opioids, preventing euphoria and reducing cravings.",
        how_it_works="Blocks opioid receptors, preventing opioids from producing euphoric effects and reducing reward pathways associated with drug use.",
        typical_duration="6-12 months or longer",
        evidence_level=EvidenceLevel.HIGH,
        effectiveness_rating=7,
        success_rate="25-30% completion rates, higher with injection form",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=[
            "Nausea", "Headache", "Dizziness", "Fatigue",
            "Anxiety", "Sleep difficulties", "Injection site reactions (Vivitrol)"
        ],
        contraindications=[
            "Current opioid dependence", "Acute hepatitis",
            "Liver failure", "Recent opioid use (7-10 days)"
        ],
        accessibility=AccessibilityLevel.PRESCRIPTION_ONLY,
        cost_range="$1,000-$1,500 per month (injection)",
        insurance_coverage="Often covered by insurance",
        requirements=[
            "Complete detoxification first", "7-10 days opioid-free",
            "Medical evaluation", "Regular monitoring"
        ],
        where_to_find=[
            "Addiction medicine specialists", "Psychiatrists",
            "Primary care providers", "Treatment centers"
        ],
        can_combine_with=[
            "All forms of counseling and therapy",
            "Support groups", "Other non-opioid medications"
        ],
        cannot_combine_with=[
            "Any opioid medications", "Opioid-based pain relievers"
        ],
        pros=[
            "Blocks euphoric effects of opioids", "Monthly injection option",
            "No potential for diversion", "Effective for motivated individuals"
        ],
        cons=[
            "Requires complete detox first", "No effect on withdrawal",
            "High dropout rates", "Risk if opioids used",
            "Expensive"
        ],
        best_for=[
            "Highly motivated individuals", "Those who have completed detox",
            "People with good social support", "Court-mandated treatment"
        ],
        not_recommended_for=[
            "Those currently using opioids", "People with liver disease",
            "Those needing pain medication", "Pregnant women"
        ],
        resources=[
            "Vivitrol manufacturer resources",
            "SAMHSA treatment locator"
        ]
    ),

    # Behavioral Therapies
    "cognitive_behavioral_therapy": RecoveryMethod(
        id="cognitive_behavioral_therapy",
        name="Cognitive Behavioral Therapy (CBT)",
        category=MethodCategory.BEHAVIORAL_THERAPY,
        description="Structured therapy focusing on identifying and changing negative thought patterns and behaviors that contribute to substance use.",
        how_it_works="Helps individuals recognize triggers, develop coping strategies, and modify thoughts and behaviors that lead to drug use.",
        typical_duration="12-16 sessions over 3-4 months",
        evidence_level=EvidenceLevel.HIGH,
        effectiveness_rating=7,
        success_rate="40-60% when combined with other treatments",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=["Temporary emotional discomfort", "Initial anxiety"],
        contraindications=["Acute psychosis", "Severe cognitive impairment"],
        accessibility=AccessibilityLevel.MODERATE,
        cost_range="$100-$200 per session",
        insurance_coverage="Usually covered by health insurance",
        requirements=[
            "Commitment to regular sessions", "Willingness to complete homework",
            "Basic cognitive functioning"
        ],
        where_to_find=[
            "Licensed therapists", "Mental health centers",
            "Addiction treatment programs", "Private practice"
        ],
        can_combine_with=[
            "All MAT options", "Support groups", "Other therapies",
            "Psychiatric medications"
        ],
        cannot_combine_with=[],
        pros=[
            "Evidence-based approach", "Teaches lifelong skills",
            "Addresses underlying issues", "Can prevent relapse"
        ],
        cons=[
            "Requires active participation", "May take time to see results",
            "Can be emotionally challenging"
        ],
        best_for=[
            "Individuals committed to change", "Those with depression/anxiety",
            "People who like structured approaches"
        ],
        not_recommended_for=[
            "Those in active withdrawal", "Severely cognitively impaired",
            "People not ready for change"
        ],
        resources=[
            "Psychology Today provider directory",
            "Association for Behavioral and Cognitive Therapies"
        ]
    ),

    "contingency_management": RecoveryMethod(
        id="contingency_management",
        name="Contingency Management",
        category=MethodCategory.BEHAVIORAL_THERAPY,
        description="Behavioral intervention that provides tangible rewards for positive behaviors like maintaining sobriety or attending treatment.",
        how_it_works="Uses positive reinforcement principles by providing immediate rewards for drug-negative urine tests and treatment participation.",
        typical_duration="12-24 weeks",
        evidence_level=EvidenceLevel.HIGH,
        effectiveness_rating=8,
        success_rate="Significantly improves treatment retention and abstinence",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=["Potential dependency on external rewards"],
        contraindications=[],
        accessibility=AccessibilityLevel.LIMITED,
        cost_range="Varies by program",
        insurance_coverage="Limited coverage",
        requirements=[
            "Participation in treatment program",
            "Regular drug testing", "Goal setting"
        ],
        where_to_find=[
            "Specialized treatment programs", "Research-based clinics",
            "Some community treatment centers"
        ],
        can_combine_with=[
            "All other treatment approaches", "MAT", "Counseling"
        ],
        cannot_combine_with=[],
        pros=[
            "Highly effective", "Motivates positive behavior",
            "Improves treatment retention", "Evidence-based"
        ],
        cons=[
            "Limited availability", "May not work long-term without rewards",
            "Requires structured program"
        ],
        best_for=[
            "Individuals motivated by rewards", "Those in early recovery",
            "People with poor treatment adherence"
        ],
        not_recommended_for=[
            "Those opposed to reward systems",
            "People without access to programs"
        ],
        resources=[
            "Center for Addiction Medicine",
            "NIDA Contingency Management resources"
        ]
    ),

    # Support Groups
    "narcotics_anonymous": RecoveryMethod(
        id="narcotics_anonymous",
        name="Narcotics Anonymous (NA)",
        category=MethodCategory.SUPPORT_GROUPS,
        description="12-step fellowship program for people recovering from drug addiction, based on spiritual principles and peer support.",
        how_it_works="Members work through 12 steps with a sponsor, attend regular meetings, and support each other through shared experiences and spiritual growth.",
        typical_duration="Ongoing, lifelong participation encouraged",
        evidence_level=EvidenceLevel.MODERATE,
        effectiveness_rating=6,
        success_rate="Variable, higher with longer participation",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=["Potential religious/spiritual conflicts"],
        contraindications=[],
        accessibility=AccessibilityLevel.HIGH,
        cost_range="Free (donations accepted)",
        insurance_coverage="N/A - Free program",
        requirements=[
            "Desire to stop using drugs", "Willingness to attend meetings",
            "Open to spiritual concepts"
        ],
        where_to_find=[
            "Community centers", "Churches", "Hospitals",
            "Online meetings", "NA website meeting locator"
        ],
        can_combine_with=[
            "All forms of treatment", "MAT", "Therapy",
            "Medical treatment"
        ],
        cannot_combine_with=[],
        pros=[
            "Free and widely available", "Peer support network",
            "24/7 availability", "Spiritual component",
            "Long history of helping people"
        ],
        cons=[
            "Spiritual/religious focus may not suit everyone",
            "Variable meeting quality", "Abstinence-only approach",
            "May discourage medication-assisted treatment"
        ],
        best_for=[
            "Those seeking peer support", "People open to spiritual growth",
            "Individuals wanting long-term support network"
        ],
        not_recommended_for=[
            "Those opposed to spiritual concepts",
            "People preferring secular approaches"
        ],
        resources=[
            "Narcotics Anonymous World Services",
            "Local NA meeting schedules"
        ]
    ),

    "smart_recovery": RecoveryMethod(
        id="smart_recovery",
        name="SMART Recovery",
        category=MethodCategory.SUPPORT_GROUPS,
        description="Self-management and recovery training program using cognitive-behavioral and motivational tools without spiritual components.",
        how_it_works="Uses 4-point program focusing on motivation, coping with urges, managing thoughts and behaviors, and living a balanced life.",
        typical_duration="Self-determined, typically months to years",
        evidence_level=EvidenceLevel.MODERATE,
        effectiveness_rating=7,
        success_rate="Comparable to 12-step programs",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=[],
        contraindications=[],
        accessibility=AccessibilityLevel.MODERATE,
        cost_range="Free meetings, small fee for materials",
        insurance_coverage="N/A - Free program",
        requirements=[
            "Motivation to change", "Willingness to use tools",
            "Basic literacy for materials"
        ],
        where_to_find=[
            "Community centers", "Hospitals", "Treatment centers",
            "Online meetings", "SMART Recovery website"
        ],
        can_combine_with=[
            "All forms of treatment", "MAT", "Therapy",
            "Medical treatment"
        ],
        cannot_combine_with=[],
        pros=[
            "Science-based approach", "No spiritual requirements",
            "Supports harm reduction", "Practical tools",
            "Self-empowerment focus"
        ],
        cons=[
            "Less available than 12-step programs",
            "Requires more self-direction",
            "May be too structured for some"
        ],
        best_for=[
            "Those preferring scientific approaches",
            "Self-motivated individuals",
            "People seeking practical tools"
        ],
        not_recommended_for=[
            "Those wanting spiritual component",
            "People needing highly structured support"
        ],
        resources=[
            "SMART Recovery International",
            "Online SMART Recovery tools"
        ]
    ),

    # Harm Reduction
    "needle_exchange": RecoveryMethod(
        id="needle_exchange",
        name="Needle Exchange Programs",
        category=MethodCategory.HARM_REDUCTION,
        description="Programs that provide clean needles and syringes to reduce infection risk and provide access to health services and treatment referrals.",
        how_it_works="Reduces transmission of bloodborne diseases by providing sterile injection equipment and serves as entry point to healthcare and treatment services.",
        typical_duration="Ongoing as needed",
        evidence_level=EvidenceLevel.HIGH,
        effectiveness_rating=9,
        success_rate="Highly effective at reducing HIV/Hepatitis transmission",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=[],
        contraindications=[],
        accessibility=AccessibilityLevel.MODERATE,
        cost_range="Free to participants",
        insurance_coverage="N/A - Public health funded",
        requirements=["Active injection drug use"],
        where_to_find=[
            "Public health departments", "Community health centers",
            "Mobile units", "Harm reduction organizations"
        ],
        can_combine_with=[
            "All forms of treatment", "Medical care",
            "Mental health services"
        ],
        cannot_combine_with=[],
        pros=[
            "Prevents infectious disease", "No requirement to stop using",
            "Connects people to services", "Saves lives",
            "Cost-effective public health measure"
        ],
        cons=[
            "Does not address addiction directly",
            "May face community opposition",
            "Limited availability in some areas"
        ],
        best_for=[
            "Active injection drug users", "People not ready for treatment",
            "Those at high risk for infections"
        ],
        not_recommended_for=[
            "Non-injection drug users"
        ],
        resources=[
            "North American Syringe Exchange Network",
            "Local health departments"
        ]
    ),

    "naloxone": RecoveryMethod(
        id="naloxone",
        name="Naloxone (Narcan)",
        category=MethodCategory.HARM_REDUCTION,
        description="Overdose reversal medication that can rapidly reverse opioid overdose and save lives.",
        how_it_works="Opioid antagonist that displaces opioids from brain receptors, temporarily reversing overdose effects.",
        typical_duration="Effects last 30-90 minutes",
        evidence_level=EvidenceLevel.HIGH,
        effectiveness_rating=10,
        success_rate="Highly effective when administered properly",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=[
            "Precipitated withdrawal in dependent users",
            "Nausea", "Headache", "Dizziness"
        ],
        contraindications=["Known hypersensitivity"],
        accessibility=AccessibilityLevel.HIGH,
        cost_range="Free from many programs, $20-40 retail",
        insurance_coverage="Often covered, available over-the-counter",
        requirements=[
            "Basic training on administration",
            "Knowledge of overdose signs"
        ],
        where_to_find=[
            "Pharmacies", "Emergency services", "Treatment programs",
            "Community organizations", "Health departments"
        ],
        can_combine_with=[
            "All treatment approaches", "Emergency services"
        ],
        cannot_combine_with=[],
        pros=[
            "Saves lives immediately", "Easy to administer",
            "Widely available", "Relatively inexpensive",
            "No prescription needed in many areas"
        ],
        cons=[
            "Temporary effect only", "Can cause withdrawal",
            "Requires someone to administer",
            "May give false sense of safety"
        ],
        best_for=[
            "Anyone at risk of overdose", "Family and friends of users",
            "People using opioids", "First responders"
        ],
        not_recommended_for=[
            "Those with known allergies to naloxone"
        ],
        resources=[
            "SAMHSA Opioid Overdose Toolkit",
            "GetNaloxoneNow.org"
        ]
    ),

    # Alternative/Complementary Methods
    "acupuncture": RecoveryMethod(
        id="acupuncture",
        name="Acupuncture",
        category=MethodCategory.ALTERNATIVE_COMPLEMENTARY,
        description="Traditional Chinese medicine practice involving insertion of thin needles at specific points, often used as adjunct treatment for addiction.",
        how_it_works="May help reduce cravings, anxiety, and withdrawal symptoms through stimulation of nervous system and endorphin release.",
        typical_duration="Multiple sessions over weeks to months",
        evidence_level=EvidenceLevel.LIMITED,
        effectiveness_rating=5,
        success_rate="Mixed results in studies",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=[
            "Minor bleeding", "Bruising", "Infection (rare)",
            "Dizziness", "Temporary pain at needle sites"
        ],
        contraindications=[
            "Bleeding disorders", "Use of blood thinners",
            "Severe immunodeficiency", "Pregnancy (certain points)"
        ],
        accessibility=AccessibilityLevel.MODERATE,
        cost_range="$60-$120 per session",
        insurance_coverage="Some plans cover acupuncture",
        requirements=[
            "Licensed acupuncturist", "Multiple sessions",
            "Open mind to alternative approaches"
        ],
        where_to_find=[
            "Licensed acupuncturists", "Integrative medicine centers",
            "Some addiction treatment programs"
        ],
        can_combine_with=[
            "All conventional treatments", "MAT", "Counseling"
        ],
        cannot_combine_with=[],
        pros=[
            "Non-pharmaceutical approach", "May reduce anxiety",
            "Holistic treatment", "Few side effects",
            "Can be relaxing"
        ],
        cons=[
            "Limited scientific evidence", "Requires multiple sessions",
            "Can be expensive", "Not covered by all insurance"
        ],
        best_for=[
            "Those seeking complementary approaches",
            "People with anxiety", "Those open to alternative medicine"
        ],
        not_recommended_for=[
            "Those with bleeding disorders",
            "People seeking only evidence-based treatments"
        ],
        resources=[
            "National Certification Commission for Acupuncture",
            "American Association of Acupuncture and Oriental Medicine"
        ]
    ),

    "yoga_meditation": RecoveryMethod(
        id="yoga_meditation",
        name="Yoga and Meditation",
        category=MethodCategory.HOLISTIC_WELLNESS,
        description="Mind-body practices that combine physical postures, breathing techniques, and meditation to support recovery.",
        how_it_works="Reduces stress, improves emotional regulation, increases body awareness, and provides healthy coping mechanisms.",
        typical_duration="Ongoing practice, daily recommended",
        evidence_level=EvidenceLevel.MODERATE,
        effectiveness_rating=6,
        success_rate="Positive effects on stress reduction and wellbeing",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=[
            "Minor muscle soreness", "Possible injury with advanced poses",
            "Emotional release during practice"
        ],
        contraindications=[
            "Severe physical limitations", "Acute psychosis",
            "Recent surgery (depending on type)"
        ],
        accessibility=AccessibilityLevel.HIGH,
        cost_range="Free (online/apps) to $20-30 per class",
        insurance_coverage="Some plans cover yoga classes",
        requirements=[
            "Basic physical mobility", "Willingness to practice",
            "Comfortable clothing"
        ],
        where_to_find=[
            "Yoga studios", "Community centers", "Treatment programs",
            "Online platforms", "Apps", "Books"
        ],
        can_combine_with=[
            "All other treatments", "MAT", "Therapy"
        ],
        cannot_combine_with=[],
        pros=[
            "Improves physical and mental health",
            "Teaches stress management", "Builds community",
            "Low cost options available", "Holistic approach"
        ],
        cons=[
            "May not address addiction directly",
            "Requires regular practice", "Physical limitations may apply"
        ],
        best_for=[
            "Those seeking holistic approaches",
            "People with stress and anxiety",
            "Individuals wanting physical activity"
        ],
        not_recommended_for=[
            "Those with severe physical limitations",
            "People in acute withdrawal"
        ],
        resources=[
            "Yoga Alliance", "Y12SR (Yoga of 12-Step Recovery)",
            "Mindfulness-based addiction treatment programs"
        ]
    ),

    # Crisis/Emergency Methods
    "crisis_hotlines": RecoveryMethod(
        id="crisis_hotlines",
        name="Crisis Hotlines and Emergency Support",
        category=MethodCategory.CRISIS_EMERGENCY,
        description="24/7 telephone and text support services for people in crisis or needing immediate help with addiction or mental health issues.",
        how_it_works="Trained counselors provide immediate emotional support, crisis intervention, safety planning, and referrals to local resources.",
        typical_duration="Individual calls vary, ongoing availability",
        evidence_level=EvidenceLevel.HIGH,
        effectiveness_rating=9,
        success_rate="Effective for crisis de-escalation and connection to services",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=[],
        contraindications=[],
        accessibility=AccessibilityLevel.HIGH,
        cost_range="Free",
        insurance_coverage="N/A - Free service",
        requirements=[
            "Access to phone or text capability"
        ],
        where_to_find=[
            "National hotlines", "Local crisis centers",
            "Online chat services", "Text services"
        ],
        can_combine_with=[
            "All other treatments and services"
        ],
        cannot_combine_with=[],
        pros=[
            "Available 24/7", "Free and confidential",
            "Immediate access", "Trained counselors",
            "Can provide local referrals"
        ],
        cons=[
            "Not a replacement for ongoing treatment",
            "May have wait times", "Dependent on phone access"
        ],
        best_for=[
            "Anyone in crisis", "People needing immediate support",
            "Those seeking information about treatment"
        ],
        not_recommended_for=[
            "Medical emergencies (call 911 instead)"
        ],
        resources=[
            "National Suicide Prevention Lifeline: 988",
            "SAMHSA National Helpline: 1-800-662-4357",
            "Crisis Text Line: Text HOME to 741741"
        ]
    ),

    # Experimental/Controversial Methods
    "ibogaine": RecoveryMethod(
        id="ibogaine",
        name="Ibogaine Treatment",
        category=MethodCategory.ALTERNATIVE_COMPLEMENTARY,
        description="Psychoactive substance derived from African plant, used in some countries for addiction treatment but illegal in the US.",
        how_it_works="May reset neurotransmitter systems and provide introspective experiences that reduce addiction cravings.",
        typical_duration="Single intensive treatment over 24-48 hours",
        evidence_level=EvidenceLevel.EXPERIMENTAL,
        effectiveness_rating=4,
        success_rate="Anecdotal reports vary widely",
        safety_level=SafetyLevel.HIGH_RISK,
        risks_side_effects=[
            "Cardiac complications", "Seizures", "Death (rare but documented)",
            "Psychological distress", "Nausea and vomiting",
            "Ataxia (loss of coordination)"
        ],
        contraindications=[
            "Heart conditions", "Psychiatric disorders",
            "Liver disease", "Current medications",
            "Pregnancy", "Age under 18"
        ],
        accessibility=AccessibilityLevel.LIMITED,
        cost_range="$3,000-$15,000 (in countries where legal)",
        insurance_coverage="Not covered",
        requirements=[
            "Medical screening", "Travel to countries where legal",
            "Significant financial resources"
        ],
        where_to_find=[
            "Treatment centers in Mexico, Canada, Netherlands",
            "Underground providers (illegal in US)"
        ],
        can_combine_with=[
            "Aftercare counseling", "Integration therapy"
        ],
        cannot_combine_with=[
            "Most medications", "Other psychoactive substances"
        ],
        pros=[
            "May provide rapid interruption of addiction",
            "Some report lasting effects", "Addresses psychological aspects"
        ],
        cons=[
            "Illegal in US", "High risk of complications",
            "Expensive", "Limited scientific evidence",
            "Requires travel", "No regulation"
        ],
        best_for=[
            "Those who have exhausted other options",
            "Individuals able to travel abroad",
            "People with financial resources"
        ],
        not_recommended_for=[
            "Those with heart conditions", "Pregnant women",
            "People with psychiatric disorders",
            "Anyone seeking safe, proven treatments"
        ],
        resources=[
            "Global Ibogaine Therapy Alliance",
            "Medical literature and case studies"
        ]
    ),

    "kratom": RecoveryMethod(
        id="kratom",
        name="Kratom",
        category=MethodCategory.ALTERNATIVE_COMPLEMENTARY,
        description="Plant-based substance with opioid-like properties, used by some for self-treatment of opioid withdrawal.",
        how_it_works="Contains alkaloids that bind to opioid receptors, potentially reducing withdrawal symptoms and cravings.",
        typical_duration="Variable, from days to ongoing use",
        evidence_level=EvidenceLevel.CONTROVERSIAL,
        effectiveness_rating=4,
        success_rate="Anecdotal reports vary, limited scientific data",
        safety_level=SafetyLevel.HIGH_RISK,
        risks_side_effects=[
            "Potential for dependence", "Liver damage",
            "Nausea", "Constipation", "Weight loss",
            "Seizures (rare)", "Psychosis (rare)"
        ],
        contraindications=[
            "Liver disease", "Psychiatric disorders",
            "Pregnancy", "Use with other substances"
        ],
        accessibility=AccessibilityLevel.MODERATE,
        cost_range="$20-$100 per month",
        insurance_coverage="Not covered",
        requirements=[
            "Available in states where legal",
            "Age 18 or older"
        ],
        where_to_find=[
            "Head shops", "Online vendors", "Botanical stores"
        ],
        can_combine_with=[
            "Counseling and therapy (with caution)"
        ],
        cannot_combine_with=[
            "Alcohol", "Benzodiazepines", "Other opioids"
        ],
        pros=[
            "May reduce withdrawal symptoms",
            "Legal in many states", "Less expensive than some treatments"
        ],
        cons=[
            "Not FDA approved", "Potential for dependence",
            "Quality varies", "Limited research",
            "Legal status varies by location"
        ],
        best_for=[
            "Those seeking alternative approaches",
            "People in areas with limited treatment access"
        ],
        not_recommended_for=[
            "Those with liver disease", "Pregnant women",
            "People with psychiatric conditions",
            "Those seeking FDA-approved treatments"
        ],
        resources=[
            "American Kratom Association",
            "Academic research on kratom"
        ]
    ),

    # =====================================================
    # PEER SUPPORT METHODS
    # =====================================================
    
    "recovery_coaching": RecoveryMethod(
        id="recovery_coaching",
        name="Recovery Coaching",
        category=MethodCategory.PEER_SUPPORT,
        description="Trained individuals with lived experience who provide personalized support, guidance, and accountability throughout the recovery journey.",
        how_it_works="Recovery coaches work one-on-one with individuals to set goals, navigate challenges, connect with resources, and provide ongoing encouragement based on their own recovery experience.",
        typical_duration="Ongoing, typically 6-12 months or longer",
        evidence_level=EvidenceLevel.MODERATE,
        effectiveness_rating=7,
        success_rate="Studies show improved treatment retention and recovery outcomes",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=["Dependency on coach relationship"],
        contraindications=[],
        accessibility=AccessibilityLevel.MODERATE,
        cost_range="Free through some programs, $50-$150/hour private",
        insurance_coverage="Some Medicaid programs and insurers cover peer support",
        requirements=[
            "Willingness to engage with a coach",
            "Commitment to recovery goals"
        ],
        where_to_find=[
            "Treatment centers", "Recovery community organizations",
            "State peer support programs", "Private practice coaches",
            "SAMHSA treatment locator"
        ],
        can_combine_with=["All other treatment methods", "MAT", "Therapy", "Support groups"],
        cannot_combine_with=[],
        pros=[
            "Lived experience provides unique understanding",
            "Non-clinical, peer-based approach",
            "Flexible and personalized support",
            "Can help navigate recovery system",
            "Available in many communities"
        ],
        cons=[
            "Quality varies by coach training",
            "Not a substitute for clinical treatment",
            "May have limited availability"
        ],
        best_for=[
            "Those seeking peer support with lived experience",
            "People navigating early recovery",
            "Individuals needing help accessing services"
        ],
        not_recommended_for=[
            "Those requiring clinical mental health treatment",
            "People in acute medical crisis"
        ],
        resources=[
            "Connecticut Community for Addiction Recovery (CCAR)",
            "Faces and Voices of Recovery",
            "State recovery community organizations"
        ]
    ),

    "peer_support_specialist": RecoveryMethod(
        id="peer_support_specialist",
        name="Peer Support Specialist Services",
        category=MethodCategory.PEER_SUPPORT,
        description="Certified professionals with personal recovery experience who provide emotional support, share knowledge, and help connect individuals to community resources.",
        how_it_works="Peer support specialists use their lived experience combined with formal training to offer hope, share coping strategies, and assist with recovery planning in clinical or community settings.",
        typical_duration="Ongoing support throughout recovery journey",
        evidence_level=EvidenceLevel.MODERATE,
        effectiveness_rating=7,
        success_rate="Associated with reduced hospitalizations and improved engagement",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=[],
        contraindications=[],
        accessibility=AccessibilityLevel.MODERATE,
        cost_range="Often free or covered by insurance",
        insurance_coverage="Covered by Medicaid in most states",
        requirements=[
            "Enrollment in treatment program or healthcare system",
            "Openness to peer support"
        ],
        where_to_find=[
            "Community mental health centers",
            "Hospital systems", "Recovery community centers",
            "Peer-run organizations", "Treatment programs"
        ],
        can_combine_with=["All treatment modalities"],
        cannot_combine_with=[],
        pros=[
            "Certified training ensures quality",
            "Often covered by insurance",
            "Integrated into healthcare systems",
            "Reduces stigma through shared experience",
            "Improves treatment engagement"
        ],
        cons=[
            "Availability varies by location",
            "May have limited hours",
            "Requires program enrollment in some cases"
        ],
        best_for=[
            "Those in treatment programs",
            "People wanting peer support within healthcare",
            "Individuals seeking certified peer professionals"
        ],
        not_recommended_for=[],
        resources=[
            "National Association of Peer Supporters (N.A.P.S.)",
            "International Association of Peer Supporters",
            "State certification programs"
        ]
    ),

    "recovery_community_center": RecoveryMethod(
        id="recovery_community_center",
        name="Recovery Community Centers",
        category=MethodCategory.PEER_SUPPORT,
        description="Peer-operated centers that provide a safe, supportive environment and recovery resources without requiring clinical treatment or abstinence.",
        how_it_works="Centers offer drop-in services, social activities, peer support, recovery meetings, educational workshops, and connections to treatment and social services.",
        typical_duration="Open-ended; members use services as needed",
        evidence_level=EvidenceLevel.MODERATE,
        effectiveness_rating=6,
        success_rate="Shown to improve recovery capital and community connection",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=[],
        contraindications=[],
        accessibility=AccessibilityLevel.HIGH,
        cost_range="Free",
        insurance_coverage="N/A - Free community service",
        requirements=["None - open to all seeking recovery support"],
        where_to_find=[
            "Community locations nationwide",
            "Association of Recovery Community Organizations directory",
            "State recovery community organizations"
        ],
        can_combine_with=["All recovery approaches"],
        cannot_combine_with=[],
        pros=[
            "Free and accessible",
            "No clinical requirements",
            "Welcoming of all recovery pathways",
            "Community and social connection",
            "Peer-run environment"
        ],
        cons=[
            "Not available in all areas",
            "Quality varies by center",
            "Not clinical treatment"
        ],
        best_for=[
            "Anyone seeking community support",
            "Those in any stage of recovery",
            "People wanting non-clinical resources"
        ],
        not_recommended_for=[
            "Those needing acute clinical care"
        ],
        resources=[
            "Association of Recovery Community Organizations (ARCO)",
            "Faces and Voices of Recovery",
            "Local recovery community organizations"
        ]
    ),

    # =====================================================
    # ADDITIONAL HARM REDUCTION METHODS
    # =====================================================

    "fentanyl_test_strips": RecoveryMethod(
        id="fentanyl_test_strips",
        name="Fentanyl Test Strips",
        category=MethodCategory.HARM_REDUCTION,
        description="Inexpensive testing strips that detect the presence of fentanyl and its analogs in drug supplies to help prevent accidental overdose.",
        how_it_works="Test strips use immunoassay technology to detect fentanyl in a small sample of drugs dissolved in water, providing results in 2-5 minutes.",
        typical_duration="Single use per test",
        evidence_level=EvidenceLevel.HIGH,
        effectiveness_rating=8,
        success_rate="Studies show users who test positive are more likely to use harm reduction strategies",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=[
            "False negatives possible with novel analogs",
            "May not detect all fentanyl in uneven mixture"
        ],
        contraindications=[],
        accessibility=AccessibilityLevel.MODERATE,
        cost_range="$1-2 per strip, often free from harm reduction programs",
        insurance_coverage="Not covered, but widely distributed free",
        requirements=["Basic instructions on use"],
        where_to_find=[
            "Harm reduction organizations",
            "Needle exchange programs",
            "Some pharmacies",
            "Health departments",
            "Online vendors"
        ],
        can_combine_with=["All other harm reduction approaches", "Any treatment"],
        cannot_combine_with=[],
        pros=[
            "Inexpensive and easy to use",
            "Can prevent fatal overdoses",
            "Empowers informed decision-making",
            "Quick results",
            "Highly accurate for common fentanyl"
        ],
        cons=[
            "May miss novel fentanyl analogs",
            "Requires drug sample mixing",
            "Legal status varies by state",
            "False sense of security if negative"
        ],
        best_for=[
            "Anyone using drugs that may be contaminated",
            "People using street drugs",
            "Harm reduction outreach workers"
        ],
        not_recommended_for=[],
        resources=[
            "DanceSafe", "NEXT Distro",
            "Local harm reduction organizations",
            "Health departments"
        ]
    ),

    "safe_consumption_sites": RecoveryMethod(
        id="safe_consumption_sites",
        name="Safe Consumption Sites (Supervised Injection Facilities)",
        category=MethodCategory.HARM_REDUCTION,
        description="Legally sanctioned facilities where people can use pre-obtained drugs under medical supervision, with overdose prevention and access to health services.",
        how_it_works="Trained staff supervise drug use, provide clean equipment, reverse overdoses immediately, and connect people to treatment, housing, and healthcare services.",
        typical_duration="Single visits as needed",
        evidence_level=EvidenceLevel.HIGH,
        effectiveness_rating=9,
        success_rate="Zero overdose deaths at supervised facilities worldwide; increased treatment entry",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=[],
        contraindications=[],
        accessibility=AccessibilityLevel.LIMITED,
        cost_range="Free to users",
        insurance_coverage="N/A - Public health funded",
        requirements=["Located in jurisdiction where legal/operating"],
        where_to_find=[
            "New York City (OnPoint NYC)",
            "Rhode Island (approved)",
            "Canada (over 30 sites)",
            "Europe, Australia (numerous sites)"
        ],
        can_combine_with=["All harm reduction and treatment approaches"],
        cannot_combine_with=[],
        pros=[
            "Prevents overdose deaths",
            "Reduces disease transmission",
            "Connects users to services",
            "Reduces public drug use",
            "Provides entry to treatment"
        ],
        cons=[
            "Very limited availability in US",
            "Controversial/legal challenges",
            "Requires proximity to facility",
            "Does not provide drugs"
        ],
        best_for=[
            "Active injection drug users",
            "High-risk overdose populations",
            "Homeless individuals",
            "Those not ready for treatment"
        ],
        not_recommended_for=[],
        resources=[
            "Drug Policy Alliance",
            "National Harm Reduction Coalition",
            "OnPoint NYC"
        ]
    ),

    "safe_supply_programs": RecoveryMethod(
        id="safe_supply_programs",
        name="Safe Supply Programs",
        category=MethodCategory.HARM_REDUCTION,
        description="Programs providing pharmaceutical-grade opioids as alternatives to toxic street drugs, primarily operating in Canada to prevent overdose deaths.",
        how_it_works="Prescribers provide regulated opioids (hydromorphone, diacetylmorphine) to people at high risk of overdose, reducing exposure to fentanyl-contaminated supply.",
        typical_duration="Ongoing as prescribed",
        evidence_level=EvidenceLevel.MODERATE,
        effectiveness_rating=8,
        success_rate="Early evidence shows reduced overdose risk and emergency visits",
        safety_level=SafetyLevel.MODERATE_RISK,
        risks_side_effects=[
            "Continued opioid dependence",
            "Medical monitoring required",
            "Potential for diversion"
        ],
        contraindications=[
            "Not available in US",
            "Requires medical assessment"
        ],
        accessibility=AccessibilityLevel.LIMITED,
        cost_range="Free to participants in Canada",
        insurance_coverage="Covered in Canadian provincial programs",
        requirements=[
            "History of substance use disorder",
            "High risk of overdose",
            "Medical evaluation",
            "Program enrollment"
        ],
        where_to_find=[
            "British Columbia, Canada",
            "Ontario, Canada (various programs)",
            "Not currently available in US"
        ],
        can_combine_with=["Counseling", "Peer support", "Housing services"],
        cannot_combine_with=["Naltrexone"],
        pros=[
            "Eliminates toxic drug exposure",
            "Reduces overdose deaths",
            "Pharmaceutical-grade quality",
            "Medical supervision",
            "Reduces criminal activity"
        ],
        cons=[
            "Not available in US",
            "Maintains opioid dependence",
            "Controversial approach",
            "Limited evidence base"
        ],
        best_for=[
            "High-risk overdose populations",
            "Those who have not succeeded with MAT",
            "Homeless and marginalized populations"
        ],
        not_recommended_for=[
            "Those seeking abstinence",
            "People outside Canada/available regions"
        ],
        resources=[
            "BC Centre on Substance Use",
            "Canadian Drug Policy Coalition",
            "Drug Policy Alliance"
        ]
    ),

    "naloxone_auto_injector": RecoveryMethod(
        id="naloxone_auto_injector",
        name="Naloxone Auto-Injector (Evzio, Zimhi)",
        category=MethodCategory.HARM_REDUCTION,
        description="Pre-filled automatic injection devices that deliver naloxone for opioid overdose reversal, designed for use by people without medical training.",
        how_it_works="Auto-injectors provide voice instructions and automatically deliver naloxone via intramuscular injection when pressed against the thigh.",
        typical_duration="Effects last 30-90 minutes",
        evidence_level=EvidenceLevel.HIGH,
        effectiveness_rating=10,
        success_rate="Highly effective when administered during overdose",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=[
            "Precipitated withdrawal in dependent users",
            "Injection site reactions"
        ],
        contraindications=["Known hypersensitivity to naloxone"],
        accessibility=AccessibilityLevel.MODERATE,
        cost_range="$0-$600+ depending on version and access program",
        insurance_coverage="Often covered by insurance; free through many programs",
        requirements=["Brief training recommended"],
        where_to_find=[
            "Pharmacies", "Emergency departments",
            "Harm reduction organizations",
            "Primary care providers"
        ],
        can_combine_with=["All treatment and harm reduction approaches"],
        cannot_combine_with=[],
        pros=[
            "Easy to use with voice guidance",
            "Designed for layperson use",
            "Rapid injection delivery",
            "Long shelf life",
            "Portable and discreet"
        ],
        cons=[
            "More expensive than nasal spray",
            "Single use device",
            "Requires intramuscular injection"
        ],
        best_for=[
            "Families of people using opioids",
            "First responders",
            "Schools and workplaces",
            "Anyone at risk of overdose"
        ],
        not_recommended_for=["Those with known naloxone allergy"],
        resources=[
            "Manufacturer patient assistance programs",
            "GetNaloxoneNow.org",
            "Local health departments"
        ]
    ),

    # =====================================================
    # ADDITIONAL BEHAVIORAL THERAPIES
    # =====================================================

    "dialectical_behavior_therapy": RecoveryMethod(
        id="dialectical_behavior_therapy",
        name="Dialectical Behavior Therapy (DBT)",
        category=MethodCategory.BEHAVIORAL_THERAPY,
        description="Evidence-based therapy combining cognitive-behavioral techniques with mindfulness, focusing on emotion regulation, distress tolerance, and interpersonal skills.",
        how_it_works="DBT teaches skills in four modules: mindfulness, distress tolerance, emotion regulation, and interpersonal effectiveness, often through individual therapy and group skills training.",
        typical_duration="6-12 months comprehensive treatment; skills modules 6+ months",
        evidence_level=EvidenceLevel.HIGH,
        effectiveness_rating=8,
        success_rate="Significant reductions in substance use and self-harm behaviors",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=["Emotional intensity during treatment"],
        contraindications=[
            "Active psychosis",
            "Severe cognitive impairment"
        ],
        accessibility=AccessibilityLevel.MODERATE,
        cost_range="$100-$300 per session",
        insurance_coverage="Usually covered by health insurance",
        requirements=[
            "Commitment to weekly therapy and skills group",
            "Willingness to practice skills between sessions"
        ],
        where_to_find=[
            "DBT-certified therapists",
            "Mental health centers",
            "Addiction treatment programs",
            "Psychology Today therapist directory"
        ],
        can_combine_with=["MAT", "Support groups", "Psychiatric medications"],
        cannot_combine_with=[],
        pros=[
            "Evidence-based for co-occurring disorders",
            "Teaches practical coping skills",
            "Addresses emotion dysregulation",
            "Effective for trauma survivors",
            "Reduces relapse risk"
        ],
        cons=[
            "Intensive time commitment",
            "Requires specialized training",
            "May not be available everywhere",
            "Can be emotionally challenging"
        ],
        best_for=[
            "Those with emotion regulation difficulties",
            "Individuals with co-occurring borderline personality",
            "People with trauma histories",
            "Those with self-harm behaviors"
        ],
        not_recommended_for=[
            "Those unable to commit to intensive treatment",
            "People in acute psychosis"
        ],
        resources=[
            "Behavioral Tech (Linehan Institute)",
            "DBT-Linehan Board of Certification",
            "Psychology Today DBT therapist search"
        ]
    ),

    "motivational_enhancement_therapy": RecoveryMethod(
        id="motivational_enhancement_therapy",
        name="Motivational Enhancement Therapy (MET)",
        category=MethodCategory.BEHAVIORAL_THERAPY,
        description="Brief, client-centered approach that rapidly builds internal motivation for change and develops a plan for achieving recovery goals.",
        how_it_works="Uses motivational interviewing techniques across 4 sessions to explore ambivalence, strengthen motivation, and create a change plan with personalized feedback.",
        typical_duration="4 sessions over 12 weeks",
        evidence_level=EvidenceLevel.HIGH,
        effectiveness_rating=7,
        success_rate="Effective in reducing substance use, particularly when combined with other treatments",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=[],
        contraindications=[],
        accessibility=AccessibilityLevel.MODERATE,
        cost_range="$100-$200 per session",
        insurance_coverage="Typically covered by insurance",
        requirements=["Willingness to explore motivation"],
        where_to_find=[
            "Addiction treatment programs",
            "Mental health centers",
            "Private therapists",
            "Primary care settings"
        ],
        can_combine_with=["All other treatment approaches", "MAT"],
        cannot_combine_with=[],
        pros=[
            "Brief and focused",
            "Non-confrontational approach",
            "Client-centered",
            "Effective early intervention",
            "Builds internal motivation"
        ],
        cons=[
            "Brief duration may be insufficient for some",
            "Requires skilled therapist",
            "Works best for those with some ambivalence"
        ],
        best_for=[
            "Those ambivalent about change",
            "People early in considering recovery",
            "Individuals resistant to treatment"
        ],
        not_recommended_for=[
            "Those already highly motivated",
            "People in acute crisis"
        ],
        resources=[
            "SAMHSA Evidence-Based Practices",
            "Motivational Interviewing Network of Trainers"
        ]
    ),

    "group_therapy": RecoveryMethod(
        id="group_therapy",
        name="Group Therapy for Addiction",
        category=MethodCategory.BEHAVIORAL_THERAPY,
        description="Structured therapy sessions with multiple participants led by trained clinicians, providing peer support, skill-building, and therapeutic processing.",
        how_it_works="Groups use various therapeutic approaches (CBT, process groups, psychoeducation) to foster mutual support, normalize experiences, and practice interpersonal skills.",
        typical_duration="Weekly sessions for 3-12 months or longer",
        evidence_level=EvidenceLevel.HIGH,
        effectiveness_rating=7,
        success_rate="Comparable to individual therapy for many outcomes",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=[
            "Potential discomfort with sharing",
            "Group dynamics challenges"
        ],
        contraindications=[
            "Severe social anxiety without preparation",
            "Active aggression or violence"
        ],
        accessibility=AccessibilityLevel.MODERATE,
        cost_range="$40-$100 per session",
        insurance_coverage="Usually covered by insurance",
        requirements=[
            "Ability to participate in group settings",
            "Agreement to confidentiality"
        ],
        where_to_find=[
            "Treatment programs",
            "Mental health centers",
            "Outpatient programs",
            "Private practice groups"
        ],
        can_combine_with=["Individual therapy", "MAT", "Support groups"],
        cannot_combine_with=[],
        pros=[
            "Peer support and connection",
            "More affordable than individual therapy",
            "Normalizes recovery experiences",
            "Provides multiple perspectives",
            "Builds social skills"
        ],
        cons=[
            "Less individual attention",
            "Requires group participation comfort",
            "Fixed schedule requirements"
        ],
        best_for=[
            "Those benefiting from peer connection",
            "People seeking affordable therapy",
            "Individuals wanting multiple perspectives"
        ],
        not_recommended_for=[
            "Those with severe social anxiety",
            "People unable to maintain confidentiality"
        ],
        resources=[
            "SAMHSA treatment locator",
            "American Group Psychotherapy Association"
        ]
    ),

    "motivational_interviewing": RecoveryMethod(
        id="motivational_interviewing",
        name="Motivational Interviewing (MI)",
        category=MethodCategory.BEHAVIORAL_THERAPY,
        description="Collaborative conversation style that strengthens motivation and commitment to change by exploring and resolving ambivalence.",
        how_it_works="Therapists use open questions, affirmations, reflections, and summaries (OARS) to help clients discover their own reasons for change and build confidence.",
        typical_duration="1-4 sessions, or integrated into ongoing treatment",
        evidence_level=EvidenceLevel.HIGH,
        effectiveness_rating=7,
        success_rate="Moderate effects on substance use outcomes; enhances other treatments",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=[],
        contraindications=[],
        accessibility=AccessibilityLevel.HIGH,
        cost_range="Part of therapy sessions; no additional cost",
        insurance_coverage="Covered as part of therapy",
        requirements=["Openness to self-exploration"],
        where_to_find=[
            "Most addiction treatment settings",
            "Primary care offices",
            "Mental health providers",
            "Emergency departments"
        ],
        can_combine_with=["All other treatments"],
        cannot_combine_with=[],
        pros=[
            "Widely available",
            "Respectful and non-judgmental",
            "Enhances treatment engagement",
            "Brief and effective",
            "Client-centered"
        ],
        cons=[
            "Requires skilled practitioner",
            "May not be sufficient alone",
            "Works best for ambivalent individuals"
        ],
        best_for=[
            "Anyone considering change",
            "People resistant to treatment",
            "Those early in recovery process"
        ],
        not_recommended_for=[
            "Those in acute medical emergency"
        ],
        resources=[
            "Motivational Interviewing Network of Trainers (MINT)",
            "SAMHSA treatment resources"
        ]
    ),

    # =====================================================
    # RESIDENTIAL TREATMENT
    # =====================================================

    "inpatient_detox": RecoveryMethod(
        id="inpatient_detox",
        name="Inpatient Medical Detoxification",
        category=MethodCategory.MEDICAL_ASSISTED_TREATMENT,
        description="Medically supervised withdrawal management in a hospital or residential setting, providing 24/7 monitoring and medication to manage symptoms safely.",
        how_it_works="Medical staff monitor vital signs, provide medications to reduce withdrawal symptoms (e.g., buprenorphine, clonidine), and manage complications in a controlled environment.",
        typical_duration="3-7 days for opioid detox",
        evidence_level=EvidenceLevel.HIGH,
        effectiveness_rating=7,
        success_rate="High completion rates; relapse common without continued treatment",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=[
            "Discomfort during withdrawal",
            "Reduced tolerance increases overdose risk if relapse occurs"
        ],
        contraindications=[],
        accessibility=AccessibilityLevel.SPECIALIZED_CARE,
        cost_range="$500-$2,000+ per day",
        insurance_coverage="Often covered by insurance for medical necessity",
        requirements=[
            "Physical dependence on opioids",
            "Medical evaluation",
            "Insurance authorization or payment"
        ],
        where_to_find=[
            "Hospitals", "Detox facilities",
            "Residential treatment centers",
            "SAMHSA treatment locator"
        ],
        can_combine_with=["Should transition to ongoing treatment - MAT, therapy, residential care"],
        cannot_combine_with=[],
        pros=[
            "Safe medically supervised environment",
            "24/7 monitoring and support",
            "Medication to ease symptoms",
            "Entry point to further treatment",
            "Manages medical complications"
        ],
        cons=[
            "Expensive without insurance",
            "Does not address addiction alone",
            "High relapse risk if no follow-up",
            "Limited availability"
        ],
        best_for=[
            "Those with severe physical dependence",
            "People with medical complications",
            "Individuals needing supervised environment"
        ],
        not_recommended_for=[
            "Those who can safely detox outpatient",
            "People unwilling to engage in follow-up care"
        ],
        resources=[
            "SAMHSA National Helpline: 1-800-662-4357",
            "ASAM Patient Placement Criteria"
        ]
    ),

    "residential_rehab": RecoveryMethod(
        id="residential_rehab",
        name="Residential Rehabilitation (Inpatient Rehab)",
        category=MethodCategory.MEDICAL_ASSISTED_TREATMENT,
        description="Comprehensive, structured treatment programs providing 24-hour care in a residential setting with therapy, groups, and recovery support.",
        how_it_works="Residents live on-site and participate in individual therapy, group therapy, education, life skills training, and recovery activities while separated from triggers.",
        typical_duration="28-90 days; some long-term programs 6-12 months",
        evidence_level=EvidenceLevel.HIGH,
        effectiveness_rating=8,
        success_rate="Better outcomes with longer stays; 40-60% abstinent at 1 year with follow-up",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=[
            "Separation from support systems",
            "Adjustment challenges upon return home"
        ],
        contraindications=[
            "Severe untreated psychiatric illness requiring higher care",
            "Medical conditions requiring hospital care"
        ],
        accessibility=AccessibilityLevel.SPECIALIZED_CARE,
        cost_range="$10,000-$30,000+ per month (luxury facilities much higher)",
        insurance_coverage="Often partially covered; varies significantly",
        requirements=[
            "Commitment to program length",
            "Medical/psychiatric clearance",
            "Ability to be away from home/work"
        ],
        where_to_find=[
            "Treatment centers nationwide",
            "SAMHSA treatment locator",
            "Private rehab facilities",
            "State-funded programs"
        ],
        can_combine_with=["MAT", "Therapy", "Aftercare planning"],
        cannot_combine_with=[],
        pros=[
            "Structured, immersive environment",
            "24/7 support and monitoring",
            "Removes environmental triggers",
            "Comprehensive treatment approach",
            "Builds recovery community"
        ],
        cons=[
            "Expensive, especially without insurance",
            "Requires time away from life obligations",
            "Quality varies significantly",
            "Transition home can be challenging"
        ],
        best_for=[
            "Those with severe addiction",
            "People who haven't succeeded with outpatient",
            "Individuals needing structured environment",
            "Those with unstable living situations"
        ],
        not_recommended_for=[
            "Those with strong outpatient success history",
            "People unable to leave obligations"
        ],
        resources=[
            "SAMHSA treatment locator",
            "American Addiction Centers",
            "State substance abuse agencies"
        ]
    ),

    "sober_living": RecoveryMethod(
        id="sober_living",
        name="Sober Living Homes",
        category=MethodCategory.PEER_SUPPORT,
        description="Structured, substance-free living environments that provide peer support and accountability during the transition from treatment to independent living.",
        how_it_works="Residents live together, follow house rules (drug testing, curfews, chores), attend meetings, and support each other's recovery while gradually rebuilding independent living skills.",
        typical_duration="3-12 months or longer",
        evidence_level=EvidenceLevel.MODERATE,
        effectiveness_rating=7,
        success_rate="Residents show improved outcomes with longer stays",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=[
            "Potential exposure to others in early recovery",
            "House rule violations leading to discharge"
        ],
        contraindications=[
            "Active drug use",
            "Unwillingness to follow house rules"
        ],
        accessibility=AccessibilityLevel.MODERATE,
        cost_range="$500-$2,500+ per month (varies widely by location)",
        insurance_coverage="Generally not covered; some scholarships available",
        requirements=[
            "Sobriety or commitment to sobriety",
            "Agreement to house rules",
            "Financial payment or scholarship"
        ],
        where_to_find=[
            "Oxford House network",
            "Private sober living providers",
            "Treatment center referrals",
            "Recovery community resources"
        ],
        can_combine_with=["Outpatient treatment", "MAT", "Support groups", "Employment"],
        cannot_combine_with=[],
        pros=[
            "Supportive peer environment",
            "Structure during transition",
            "More affordable than treatment",
            "Builds recovery community",
            "Gradual return to independence"
        ],
        cons=[
            "Not clinical treatment",
            "Quality varies significantly",
            "Rules may feel restrictive",
            "Cost can be barrier"
        ],
        best_for=[
            "Those transitioning from treatment",
            "People needing stable housing",
            "Individuals wanting peer accountability",
            "Those rebuilding life structure"
        ],
        not_recommended_for=[
            "Active users not ready for sobriety",
            "Those needing clinical level of care"
        ],
        resources=[
            "Oxford House",
            "National Alliance for Recovery Residences (NARR)",
            "State recovery housing resources"
        ]
    ),

    # =====================================================
    # TECHNOLOGY-BASED METHODS
    # =====================================================

    "telehealth_addiction": RecoveryMethod(
        id="telehealth_addiction",
        name="Telehealth Addiction Treatment",
        category=MethodCategory.MEDICAL_ASSISTED_TREATMENT,
        description="Remote addiction treatment services via video, phone, or app, including MAT prescribing, therapy, and recovery support.",
        how_it_works="Providers deliver evaluations, counseling, and medication management through secure video platforms, often with same-day or rapid appointments.",
        typical_duration="Ongoing treatment as needed",
        evidence_level=EvidenceLevel.HIGH,
        effectiveness_rating=8,
        success_rate="Comparable to in-person treatment for many outcomes",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=[
            "Technology barriers for some",
            "Less personal connection than in-person"
        ],
        contraindications=[
            "Lack of internet/device access",
            "Need for in-person medical procedures"
        ],
        accessibility=AccessibilityLevel.HIGH,
        cost_range="Similar to in-person care; often $100-$300 per visit",
        insurance_coverage="Widely covered post-COVID policy changes",
        requirements=[
            "Smartphone or computer with camera",
            "Internet connection",
            "Private space for sessions"
        ],
        where_to_find=[
            "Bicycle Health", "Ophelia", "Workit Health",
            "Groups Recover Together",
            "Many traditional providers now offer telehealth"
        ],
        can_combine_with=["In-person services", "Support groups", "All MAT"],
        cannot_combine_with=[],
        pros=[
            "Convenient and accessible",
            "Reduces transportation barriers",
            "Often faster access to care",
            "Can access specialists anywhere",
            "Privacy of home setting"
        ],
        cons=[
            "Requires technology access",
            "May feel less personal",
            "Not suitable for all situations",
            "Internet quality affects experience"
        ],
        best_for=[
            "Rural or underserved areas",
            "Those with transportation barriers",
            "Busy schedules or mobility issues",
            "People preferring privacy"
        ],
        not_recommended_for=[
            "Those needing in-person medical care",
            "People without technology access"
        ],
        resources=[
            "SAMHSA buprenorphine locator (telehealth filter)",
            "Telehealth addiction treatment directories",
            "State telehealth resources"
        ]
    ),

    "recovery_apps": RecoveryMethod(
        id="recovery_apps",
        name="Recovery Support Apps",
        category=MethodCategory.ALTERNATIVE_COMPLEMENTARY,
        description="Mobile applications providing tools for sobriety tracking, peer support, meditation, trigger management, and recovery resources.",
        how_it_works="Apps offer features like sobriety counters, daily check-ins, community forums, guided exercises, meeting finders, and crisis resources.",
        typical_duration="Ongoing self-directed use",
        evidence_level=EvidenceLevel.LIMITED,
        effectiveness_rating=5,
        success_rate="Limited research; user satisfaction generally positive",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=[
            "Technology replacing human connection",
            "Privacy concerns with some apps"
        ],
        contraindications=[],
        accessibility=AccessibilityLevel.HIGH,
        cost_range="Free to $15/month for premium features",
        insurance_coverage="Generally not covered",
        requirements=["Smartphone"],
        where_to_find=[
            "App stores (iOS, Android)",
            "I Am Sober", "Loosid", "Sober Grid",
            "Nomo", "Twelve Steps Companion"
        ],
        can_combine_with=["All other treatment and support"],
        cannot_combine_with=[],
        pros=[
            "Always available",
            "Free or low cost",
            "Private and discreet",
            "Community support features",
            "Tracking and motivation tools"
        ],
        cons=[
            "Limited evidence base",
            "No substitute for treatment",
            "Quality varies greatly",
            "Privacy concerns"
        ],
        best_for=[
            "Tech-savvy individuals",
            "Those wanting daily support tools",
            "People seeking community connection",
            "Those in early sobriety"
        ],
        not_recommended_for=[
            "Those needing clinical treatment",
            "People without smartphones"
        ],
        resources=[
            "App store reviews",
            "Recovery organization recommendations",
            "SAMHSA app recommendations"
        ]
    ),

    "online_therapy": RecoveryMethod(
        id="online_therapy",
        name="Online Therapy and Counseling",
        category=MethodCategory.BEHAVIORAL_THERAPY,
        description="Licensed therapy services delivered via secure video platforms, messaging, or phone, specifically addressing addiction and mental health.",
        how_it_works="Clients connect with licensed therapists through platforms offering scheduled video sessions and often asynchronous messaging between sessions.",
        typical_duration="Weekly sessions for months to years",
        evidence_level=EvidenceLevel.HIGH,
        effectiveness_rating=7,
        success_rate="Comparable to in-person therapy for many conditions",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=[
            "Technology issues can disrupt sessions",
            "Less suitable for severe crises"
        ],
        contraindications=[
            "Active suicidal ideation requiring higher care",
            "Lack of private space for sessions"
        ],
        accessibility=AccessibilityLevel.HIGH,
        cost_range="$60-$200 per session; some subscription models $250-$400/month",
        insurance_coverage="Widely covered by insurance",
        requirements=[
            "Internet connection",
            "Device with camera",
            "Private space"
        ],
        where_to_find=[
            "BetterHelp", "Talkspace",
            "Traditional therapists offering video",
            "Insurance provider directories"
        ],
        can_combine_with=["MAT", "Support groups", "In-person services"],
        cannot_combine_with=[],
        pros=[
            "Convenient scheduling",
            "No transportation needed",
            "Access to specialists",
            "Often more affordable",
            "Comfortable home environment"
        ],
        cons=[
            "Requires technology",
            "Not suitable for all crises",
            "Less personal for some",
            "Privacy requires careful setup"
        ],
        best_for=[
            "Those with busy schedules",
            "Rural area residents",
            "People preferring online communication",
            "Those with mobility limitations"
        ],
        not_recommended_for=[
            "Active crisis situations",
            "Those without private space/technology"
        ],
        resources=[
            "Psychology Today online therapy filter",
            "Insurance provider telehealth directories"
        ]
    ),

    # =====================================================
    # FAMILY SUPPORT
    # =====================================================

    "family_therapy": RecoveryMethod(
        id="family_therapy",
        name="Family Therapy for Addiction",
        category=MethodCategory.BEHAVIORAL_THERAPY,
        description="Therapeutic approaches involving family members in the treatment process to improve communication, address enabling behaviors, and support recovery.",
        how_it_works="Therapists work with the family system to improve relationships, establish healthy boundaries, address codependency, and create supportive home environments.",
        typical_duration="12-20 sessions over 3-6 months",
        evidence_level=EvidenceLevel.HIGH,
        effectiveness_rating=7,
        success_rate="Improves treatment outcomes, especially for adolescents",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=[
            "Potential for family conflict during sessions",
            "Emotional intensity"
        ],
        contraindications=[
            "Active domestic violence",
            "Family member refuses participation"
        ],
        accessibility=AccessibilityLevel.MODERATE,
        cost_range="$100-$250 per session",
        insurance_coverage="Usually covered by insurance",
        requirements=[
            "Family member participation",
            "Commitment to process"
        ],
        where_to_find=[
            "Family therapists", "Addiction treatment programs",
            "Mental health centers",
            "Private practice therapists"
        ],
        can_combine_with=["Individual therapy", "MAT", "Support groups"],
        cannot_combine_with=[],
        pros=[
            "Addresses family system",
            "Improves communication",
            "Helps family support recovery",
            "Reduces enabling behaviors",
            "Heals relationships"
        ],
        cons=[
            "Requires family participation",
            "Can surface difficult emotions",
            "Scheduling challenges",
            "Not all families willing"
        ],
        best_for=[
            "Those with family involvement in recovery",
            "Adolescents and young adults",
            "Families wanting to improve support"
        ],
        not_recommended_for=[
            "Those estranged from family",
            "Active domestic violence situations"
        ],
        resources=[
            "American Association for Marriage and Family Therapy",
            "SAMHSA family resources",
            "Treatment program family services"
        ]
    ),

    "alanon": RecoveryMethod(
        id="alanon",
        name="Al-Anon and Nar-Anon (Family Support Groups)",
        category=MethodCategory.SUPPORT_GROUPS,
        description="12-step support programs for family members and friends of people with substance use disorders, providing peer support and coping strategies.",
        how_it_works="Members attend meetings, work 12 steps adapted for families, share experiences, and support each other in dealing with a loved one's addiction.",
        typical_duration="Ongoing participation recommended",
        evidence_level=EvidenceLevel.MODERATE,
        effectiveness_rating=6,
        success_rate="Members report improved coping, reduced stress, and better family functioning",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=[],
        contraindications=[],
        accessibility=AccessibilityLevel.HIGH,
        cost_range="Free (donations accepted)",
        insurance_coverage="N/A - Free program",
        requirements=[
            "Being affected by someone's substance use",
            "Willingness to attend meetings"
        ],
        where_to_find=[
            "Community centers", "Churches",
            "Al-Anon/Nar-Anon meeting locators",
            "Online meetings"
        ],
        can_combine_with=["Family therapy", "Individual counseling", "All other approaches"],
        cannot_combine_with=[],
        pros=[
            "Free and widely available",
            "Peer support from shared experience",
            "24/7 through meetings and sponsors",
            "Teaches healthy boundaries",
            "Reduces isolation"
        ],
        cons=[
            "12-step spiritual focus may not suit all",
            "Quality varies by meeting",
            "Focus is on family member, not person using"
        ],
        best_for=[
            "Family members affected by loved one's addiction",
            "Those seeking peer support",
            "People open to 12-step approach"
        ],
        not_recommended_for=[
            "Those opposed to spiritual programs"
        ],
        resources=[
            "Al-Anon Family Groups: al-anon.org",
            "Nar-Anon Family Groups: nar-anon.org",
            "Local meeting directories"
        ]
    ),

    "family_intervention": RecoveryMethod(
        id="family_intervention",
        name="Professional Intervention",
        category=MethodCategory.CRISIS_EMERGENCY,
        description="Structured, professionally-facilitated meetings where family and friends express concern and encourage treatment entry with prearranged plans.",
        how_it_works="An intervention specialist guides the family in planning, rehearsing, and conducting a meeting where loved ones share impact of addiction and present treatment options with clear boundaries.",
        typical_duration="Preparation over days/weeks; intervention meeting 1-3 hours",
        evidence_level=EvidenceLevel.MODERATE,
        effectiveness_rating=7,
        success_rate="ARISE model shows 83% entering treatment; traditional 70-90% with professional help",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=[
            "Emotional intensity",
            "Potential damage to relationships if unsuccessful",
            "Person may resist or leave"
        ],
        contraindications=[
            "History of violence",
            "Active psychosis",
            "When person is intoxicated"
        ],
        accessibility=AccessibilityLevel.MODERATE,
        cost_range="$2,000-$15,000+ for professional interventionist",
        insurance_coverage="Not typically covered",
        requirements=[
            "Family participation",
            "Prearranged treatment plan",
            "Professional guidance recommended"
        ],
        where_to_find=[
            "Association of Intervention Specialists",
            "Treatment centers often provide",
            "Private interventionists"
        ],
        can_combine_with=["Treatment planning", "Family therapy afterward"],
        cannot_combine_with=[],
        pros=[
            "Can motivate treatment entry",
            "Professional guidance reduces risks",
            "Prearranged treatment plans",
            "Family learns healthy boundaries",
            "Can be life-saving"
        ],
        cons=[
            "Expensive",
            "No guarantee of success",
            "Can damage relationships",
            "Emotional difficulty for family"
        ],
        best_for=[
            "Families who have exhausted other options",
            "Life-threatening situations",
            "When person refuses treatment"
        ],
        not_recommended_for=[
            "Those with violent history",
            "When simpler approaches haven't been tried"
        ],
        resources=[
            "Association of Intervention Specialists",
            "ARISE intervention model",
            "Treatment center intervention services"
        ]
    ),

    # =====================================================
    # ADDITIONAL MAT OPTIONS
    # =====================================================

    "extended_release_naltrexone_implant": RecoveryMethod(
        id="extended_release_naltrexone_implant",
        name="Extended-Release Naltrexone Implant",
        category=MethodCategory.MEDICAL_ASSISTED_TREATMENT,
        description="Subcutaneous implant providing sustained naltrexone release over several months, offering longer-acting option than monthly injection.",
        how_it_works="Small implant placed under skin releases naltrexone continuously, blocking opioid receptors and preventing opioid effects for extended periods.",
        typical_duration="3-6 months per implant",
        evidence_level=EvidenceLevel.MODERATE,
        effectiveness_rating=7,
        success_rate="Limited data; may improve adherence over oral/injection",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=[
            "Implant site reactions",
            "Same risks as naltrexone",
            "Surgical implant/removal procedure"
        ],
        contraindications=[
            "Current opioid use",
            "Liver disease",
            "Need for opioid pain medication"
        ],
        accessibility=AccessibilityLevel.LIMITED,
        cost_range="$3,000-$6,000+ per implant",
        insurance_coverage="Limited coverage; some states cover",
        requirements=[
            "Complete opioid detox",
            "Medical evaluation",
            "Minor surgical procedure"
        ],
        where_to_find=[
            "Specialized addiction medicine providers",
            "Some treatment centers",
            "Research programs"
        ],
        can_combine_with=["Counseling", "Therapy", "Support groups"],
        cannot_combine_with=["Any opioid medications"],
        pros=[
            "Extended duration vs monthly shot",
            "Cannot be discontinued impulsively",
            "Improved adherence potential",
            "Less frequent medical visits"
        ],
        cons=[
            "Limited availability",
            "Requires surgical procedure",
            "Cannot use opioid pain meds",
            "Expensive with limited coverage"
        ],
        best_for=[
            "Those committed to abstinence",
            "People with adherence challenges",
            "Individuals preferring long-acting option"
        ],
        not_recommended_for=[
            "Those with chronic pain requiring opioids",
            "People not fully detoxed"
        ],
        resources=[
            "Addiction medicine specialists",
            "Research literature",
            "Manufacturer information"
        ]
    ),

    "sublocade": RecoveryMethod(
        id="sublocade",
        name="Sublocade (Extended-Release Buprenorphine)",
        category=MethodCategory.MEDICAL_ASSISTED_TREATMENT,
        description="Monthly injectable buprenorphine that provides sustained medication release, reducing need for daily oral dosing.",
        how_it_works="Monthly subcutaneous injection forms a solid depot that slowly releases buprenorphine over 4+ weeks, maintaining steady blood levels.",
        typical_duration="Monthly injections; long-term as needed",
        evidence_level=EvidenceLevel.HIGH,
        effectiveness_rating=8,
        success_rate="High retention rates; reduces illicit opioid use",
        safety_level=SafetyLevel.SAFE,
        risks_side_effects=[
            "Injection site reactions",
            "Constipation",
            "Nausea",
            "Headache"
        ],
        contraindications=[
            "Allergy to buprenorphine",
            "Severe respiratory conditions"
        ],
        accessibility=AccessibilityLevel.SPECIALIZED_CARE,
        cost_range="$1,500-$2,000 per injection",
        insurance_coverage="Often covered by insurance and Medicaid",
        requirements=[
            "Stabilization on oral buprenorphine first",
            "Monthly provider visits",
            "Administered by healthcare provider only"
        ],
        where_to_find=[
            "Addiction medicine providers",
            "Certified treatment programs",
            "SAMHSA provider locator"
        ],
        can_combine_with=["Counseling", "Therapy", "Support groups"],
        cannot_combine_with=["Full opioid agonists", "Naltrexone"],
        pros=[
            "Monthly dosing reduces diversion",
            "Steady blood levels",
            "Reduces daily medication burden",
            "Can improve treatment retention",
            "FDA-approved"
        ],
        cons=[
            "Requires monthly provider visit",
            "Injection site reactions",
            "Cannot take home",
            "Must stabilize on oral first"
        ],
        best_for=[
            "Those stable on oral buprenorphine",
            "People preferring monthly injection",
            "Individuals with adherence challenges",
            "Those concerned about diversion"
        ],
        not_recommended_for=[
            "Those new to buprenorphine treatment",
            "People preferring daily flexibility"
        ],
        resources=[
            "Sublocade manufacturer resources",
            "SAMHSA treatment locator"
        ]
    ),
}

# Crisis and emergency resources
CRISIS_RESOURCES: Dict[str, Resource] = {
    "suicide_prevention": Resource(
        id="suicide_prevention",
        title="988 Suicide & Crisis Lifeline",
        type="phone",
        description="Free, confidential 24/7 crisis support for people in suicidal crisis or emotional distress.",
        phone="988",
        category=MethodCategory.CRISIS_EMERGENCY,
        is_crisis_resource=True,
        is_free=True
    ),
    
    "samhsa_helpline": Resource(
        id="samhsa_helpline",
        title="SAMHSA National Helpline",
        type="phone",
        description="Free, confidential, 24/7 treatment referral service for individuals and families facing mental health and/or substance use disorders.",
        phone="1-800-662-4357",
        category=MethodCategory.CRISIS_EMERGENCY,
        is_crisis_resource=True,
        is_free=True
    ),
    
    "crisis_text_line": Resource(
        id="crisis_text_line",
        title="Crisis Text Line",
        type="phone",
        description="Free, 24/7 support via text message for people in crisis.",
        phone="Text HOME to 741741",
        category=MethodCategory.CRISIS_EMERGENCY,
        is_crisis_resource=True,
        is_free=True
    ),
    
    # Specialized hotlines
    "veterans_crisis": Resource(
        id="veterans_crisis",
        title="Veterans Crisis Line",
        type="phone",
        description="24/7 support for veterans, service members, and their families. Press 1 after dialing 988.",
        phone="988, then press 1",
        category=MethodCategory.CRISIS_EMERGENCY,
        is_crisis_resource=True,
        is_free=True
    ),
    
    "lgbtq_hotline": Resource(
        id="lgbtq_hotline",
        title="LGBT National Hotline",
        type="phone",
        description="Peer support, information, and local resources for LGBTQ+ individuals.",
        phone="1-888-843-4564",
        url="https://lgbthotline.org/",
        category=MethodCategory.CRISIS_EMERGENCY,
        is_crisis_resource=True,
        is_free=True
    ),
    
    "trans_lifeline": Resource(
        id="trans_lifeline",
        title="Trans Lifeline",
        type="phone",
        description="Trans-led organization connecting trans people to community, support, and resources.",
        phone="1-877-565-8860",
        url="https://translifeline.org/",
        category=MethodCategory.CRISIS_EMERGENCY,
        is_crisis_resource=True,
        is_free=True
    ),
    
    "youth_crisis": Resource(
        id="youth_crisis",
        title="National Runaway Safeline (Youth)",
        type="phone",
        description="24/7 support for youth in crisis, runaways, and families.",
        phone="1-800-786-2929",
        url="https://www.1800runaway.org/",
        category=MethodCategory.CRISIS_EMERGENCY,
        is_crisis_resource=True,
        is_free=True
    ),
    
    "teen_line": Resource(
        id="teen_line",
        title="Teen Line",
        type="phone",
        description="Teen-to-teen support line for teens in crisis. Open evenings.",
        phone="1-800-852-8336",
        url="https://teenline.org/",
        category=MethodCategory.CRISIS_EMERGENCY,
        is_crisis_resource=True,
        is_free=True
    ),
    
    "poison_control": Resource(
        id="poison_control",
        title="Poison Control Center",
        type="phone",
        description="24/7 guidance for poisoning and overdose emergencies.",
        phone="1-800-222-1222",
        category=MethodCategory.CRISIS_EMERGENCY,
        is_crisis_resource=True,
        is_free=True
    ),
    
    "nami_helpline": Resource(
        id="nami_helpline",
        title="NAMI Helpline (Mental Health)",
        type="phone",
        description="Mental health information and referrals. Mon-Fri 10am-10pm ET.",
        phone="1-800-950-6264",
        url="https://www.nami.org/help",
        category=MethodCategory.CRISIS_EMERGENCY,
        is_crisis_resource=True,
        is_free=True
    ),

    # International resources
    "international_association": Resource(
        id="international_association",
        title="International Association for Suicide Prevention",
        type="website",
        description="Directory of crisis centers worldwide with contact information by country.",
        url="https://www.iasp.info/resources/Crisis_Centres/",
        category=MethodCategory.CRISIS_EMERGENCY,
        is_crisis_resource=True,
        is_free=True
    ),
    
    "befrienders": Resource(
        id="befrienders",
        title="Befrienders Worldwide",
        type="website",
        description="Global network providing emotional support to prevent suicide. Find local centers.",
        url="https://www.befrienders.org/",
        category=MethodCategory.CRISIS_EMERGENCY,
        is_crisis_resource=True,
        is_free=True
    ),
    
    "canada_crisis": Resource(
        id="canada_crisis",
        title="Canada Suicide Prevention Service",
        type="phone",
        description="24/7 crisis support for Canada. Also text 45645.",
        phone="1-833-456-4566",
        url="https://988.ca/",
        category=MethodCategory.CRISIS_EMERGENCY,
        is_crisis_resource=True,
        is_free=True
    ),
    
    "uk_samaritans": Resource(
        id="uk_samaritans",
        title="UK Samaritans",
        type="phone",
        description="24/7 emotional support for anyone in the UK and Ireland.",
        phone="116 123",
        url="https://www.samaritans.org/",
        category=MethodCategory.CRISIS_EMERGENCY,
        is_crisis_resource=True,
        is_free=True
    ),
    
    "australia_lifeline": Resource(
        id="australia_lifeline",
        title="Lifeline Australia",
        type="phone",
        description="24/7 crisis support for Australia. Also text 0477 131 114.",
        phone="13 11 14",
        url="https://www.lifeline.org.au/",
        category=MethodCategory.CRISIS_EMERGENCY,
        is_crisis_resource=True,
        is_free=True
    ),

    # Treatment locators
    "samhsa_locator": Resource(
        id="samhsa_locator",
        title="SAMHSA Treatment Locator",
        type="website",
        description="Find treatment facilities for substance use disorders and mental health. Searchable database.",
        url="https://findtreatment.gov/",
        category=MethodCategory.CRISIS_EMERGENCY,
        is_crisis_resource=False,
        is_free=True
    ),
    
    "bupe_locator": Resource(
        id="bupe_locator",
        title="Buprenorphine Provider Locator",
        type="website",
        description="Find healthcare providers who can prescribe buprenorphine for opioid use disorder.",
        url="https://www.samhsa.gov/medication-assisted-treatment/find-treatment/treatment-practitioner-locator",
        category=MethodCategory.MEDICAL_ASSISTED_TREATMENT,
        is_crisis_resource=False,
        is_free=True
    ),
    
    "otp_locator": Resource(
        id="otp_locator",
        title="Opioid Treatment Program Locator",
        type="website",
        description="Find methadone and other opioid treatment programs (OTPs) near you.",
        url="https://dpt2.samhsa.gov/treatment/directory.aspx",
        category=MethodCategory.MEDICAL_ASSISTED_TREATMENT,
        is_crisis_resource=False,
        is_free=True
    ),
    
    "naloxone_finder": Resource(
        id="naloxone_finder",
        title="NEXT Distro - Naloxone Finder",
        type="website",
        description="Find free naloxone and harm reduction supplies near you or by mail.",
        url="https://nextdistro.org/",
        category=MethodCategory.HARM_REDUCTION,
        is_crisis_resource=False,
        is_free=True
    ),
    
    "na_meetings": Resource(
        id="na_meetings",
        title="Narcotics Anonymous Meeting Finder",
        type="website",
        description="Find NA meetings near you or online.",
        url="https://www.na.org/meetingsearch/",
        category=MethodCategory.SUPPORT_GROUPS,
        is_crisis_resource=False,
        is_free=True
    ),
    
    "smart_meetings": Resource(
        id="smart_meetings",
        title="SMART Recovery Meeting Finder",
        type="website",
        description="Find SMART Recovery meetings in person or online.",
        url="https://www.smartrecovery.org/community/",
        category=MethodCategory.SUPPORT_GROUPS,
        is_crisis_resource=False,
        is_free=True
    ),

    # Educational resources
    "nida": Resource(
        id="nida",
        title="NIDA - National Institute on Drug Abuse",
        type="website",
        description="Science-based information about drug use, addiction, and treatment.",
        url="https://nida.nih.gov/",
        category=MethodCategory.CRISIS_EMERGENCY,
        is_crisis_resource=False,
        is_free=True
    ),
    
    "harm_reduction_coalition": Resource(
        id="harm_reduction_coalition",
        title="National Harm Reduction Coalition",
        type="organization",
        description="Leading harm reduction organization with resources, training, and advocacy.",
        url="https://harmreduction.org/",
        category=MethodCategory.HARM_REDUCTION,
        is_crisis_resource=False,
        is_free=True
    ),
    
    "faces_voices": Resource(
        id="faces_voices",
        title="Faces & Voices of Recovery",
        type="organization",
        description="National recovery advocacy organization with resources and community connections.",
        url="https://facesandvoicesofrecovery.org/",
        category=MethodCategory.PEER_SUPPORT,
        is_crisis_resource=False,
        is_free=True
    ),
}

# Daily motivation quotes for recovery
DAILY_QUOTES: List[str] = [
    "Recovery is not a race. You don't have to feel guilty if it takes you longer than you thought.",
    "One day at a time. One step at a time. One moment at a time.",
    "The first step towards getting somewhere is to decide you're not going to stay where you are.",
    "Recovery is about progression, not perfection.",
    "You are not your addiction. You are a whole person deserving of love and healing.",
    "Every day is a new opportunity to change your life.",
    "Courage doesn't mean you don't get afraid. It means you don't let fear stop you.",
    "Your worst days in recovery are still better than your best days in active addiction.",
    "The opposite of addiction is not sobriety. The opposite of addiction is connection.",
    "It does not matter how slowly you go as long as you do not stop.",
    "You are braver than you believe, stronger than you seem, and smarter than you think.",
    "Fall seven times, stand up eight.",
    "Recovery is possible. Hope is real. Help is available.",
    "You don't have to see the whole staircase, just take the first step.",
    "Believe you can and you're halfway there.",
    "The only impossible journey is the one you never begin.",
    "Rock bottom became the solid foundation on which I rebuilt my life.",
    "You are worthy of the life you want to create.",
    "Asking for help is a sign of strength, not weakness.",
    "Every moment is a fresh beginning.",
    "Progress, not perfection, is what we should be asking of ourselves.",
    "You survived 100% of your worst days. You're doing great.",
    "Recovery is hard. Regret is harder. Choose your hard.",
    "The pain you feel today is the strength you'll feel tomorrow.",
    "You are allowed to be both a masterpiece and a work in progress.",
    "Sobriety delivers what addiction promises.",
    "Your life is worth more than the pain you're trying to escape.",
    "Today you are one day closer to where you want to be.",
    "Healing is not linear. Be patient with yourself.",
    "The best time to start was yesterday. The next best time is now."
]

# Coping strategies for difficult moments
COPING_STRATEGIES: List[str] = [
    "🌬️ Deep breathing: Breathe in for 4 counts, hold for 4, exhale for 4. Repeat 5 times.",
    "🧊 Hold ice cubes to ground yourself and distract from cravings.",
    "🚶 Take a walk, even just around the block. Movement helps.",
    "📞 Call someone in your support network right now.",
    "✍️ Write down what you're feeling without judgment.",
    "🎵 Listen to music that makes you feel calm or empowered.",
    "⏰ Set a timer for 15 minutes - cravings usually pass. Wait it out.",
    "💧 Drink a large glass of cold water slowly.",
    "🏃 Do 20 jumping jacks or run in place to release tension.",
    "🧘 Try a body scan: Notice sensations from head to toe.",
    "📱 Open a recovery app and read stories from others.",
    "🍫 Eat something - hunger can trigger cravings.",
    "🚿 Take a cold shower to reset your nervous system.",
    "📝 Make a list of reasons you chose recovery.",
    "🎬 Watch a funny video to shift your mental state.",
    "🧩 Do a puzzle or play a game to occupy your mind.",
    "🌳 Go outside and name 5 things you can see, 4 you can hear, 3 you can touch.",
    "💪 Remember: You've gotten through every difficult moment so far.",
    "🙏 If you pray or meditate, take 5 minutes for that now.",
    "☕ Make yourself a warm drink and sip it slowly.",
    "📖 Read something inspiring or recovery-related.",
    "🎨 Draw, color, or create something with your hands.",
    "🗣️ Say out loud: 'This feeling will pass. I am stronger than this craving.'",
    "😴 If possible, lie down and rest. Exhaustion makes everything harder.",
    "🍌 Eat a banana - potassium can help with anxiety.",
    "📝 Play it forward: Write what happens if you use vs. if you don't.",
    "🏠 Clean something small - a desk, a drawer. Small wins matter.",
    "🎧 Listen to a recovery podcast or meeting online.",
    "🤗 Give yourself a hug - self-compassion is powerful.",
    "⏪ Remember your worst day in addiction. You never have to go back there."
]

# Check-in prompts for daily reflection
CHECKIN_PROMPTS: List[str] = [
    "How are you feeling right now, on a scale of 1-10?",
    "What's one thing you're grateful for today?",
    "Did you experience any cravings today? How did you handle them?",
    "What's one healthy thing you did for yourself today?",
    "Did you reach out to anyone in your support network today?",
    "How did you sleep last night?",
    "What's one challenge you overcame today?",
    "What's one thing you're looking forward to tomorrow?",
    "Did you take your medications (if prescribed) today?",
    "What emotions came up for you today?",
    "Did you eat regular meals today?",
    "What's one kind thing you can say to yourself right now?",
    "Did anything trigger you today? What was it?",
    "What's one thing you did differently than you would have in active addiction?",
    "Who in your life are you grateful for today?",
]


def get_all_methods() -> List[RecoveryMethod]:
    """Get all recovery methods."""
    return list(RECOVERY_METHODS_DB.values())


def get_methods_by_category(category: MethodCategory) -> List[RecoveryMethod]:
    """Get all methods in a specific category."""
    return [method for method in RECOVERY_METHODS_DB.values() 
            if method.category == category]


def get_method_by_id(method_id: str) -> Optional[RecoveryMethod]:
    """Get a specific method by ID. Returns None if not found."""
    return RECOVERY_METHODS_DB.get(method_id)


def get_method_by_id_strict(method_id: str) -> RecoveryMethod:
    """Get a specific method by ID. Raises ValueError if not found."""
    if method_id not in RECOVERY_METHODS_DB:
        raise ValueError(f"Method with ID '{method_id}' not found")
    return RECOVERY_METHODS_DB[method_id]


def _get_synonym_matches(query: str) -> List[str]:
    """Get method IDs that match the query via synonyms."""
    query_lower = query.lower()
    matching_ids = []
    
    for method_id, synonyms in SEARCH_SYNONYMS.items():
        if any(query_lower in syn.lower() or syn.lower() in query_lower 
               for syn in synonyms):
            matching_ids.append(method_id)
    
    return matching_ids


def _fuzzy_match(query: str, text: str, threshold: float = 0.6) -> bool:
    """Simple fuzzy matching - checks if query is substantially contained in text."""
    query_lower = query.lower()
    text_lower = text.lower()
    
    # Direct containment
    if query_lower in text_lower:
        return True
    
    # Check word-level matching
    query_words = set(query_lower.split())
    text_words = set(text_lower.split())
    
    if query_words and len(query_words.intersection(text_words)) / len(query_words) >= threshold:
        return True
    
    return False


def search_methods(query: str, include_synonyms: bool = True, fuzzy: bool = True) -> List[RecoveryMethod]:
    """
    Search methods by name, description, or keywords.
    
    Args:
        query: Search query string
        include_synonyms: Whether to search using synonym mappings
        fuzzy: Whether to use fuzzy matching
    
    Returns:
        List of matching RecoveryMethod objects
    """
    query_lower = query.lower()
    results = []
    seen_ids = set()
    
    # First, check synonym matches
    if include_synonyms:
        synonym_matches = _get_synonym_matches(query)
        for method_id in synonym_matches:
            if method_id in RECOVERY_METHODS_DB and method_id not in seen_ids:
                results.append(RECOVERY_METHODS_DB[method_id])
                seen_ids.add(method_id)
    
    # Then do regular search
    for method in RECOVERY_METHODS_DB.values():
        if method.id in seen_ids:
            continue
            
        match_found = False
        
        # Exact containment checks
        if (query_lower in method.name.lower() or 
            query_lower in method.description.lower() or
            query_lower in method.how_it_works.lower() or
            any(query_lower in keyword.lower() for keyword in method.pros + method.cons + method.best_for)):
            match_found = True
        
        # Fuzzy matching on name
        if not match_found and fuzzy:
            if _fuzzy_match(query, method.name):
                match_found = True
        
        if match_found:
            results.append(method)
            seen_ids.add(method.id)
    
    return results


def search_methods_by_tags(tags: List[str]) -> List[RecoveryMethod]:
    """Search methods that match all given tags (in name, description, or features)."""
    if not tags:
        return []
    
    results = []
    for method in RECOVERY_METHODS_DB.values():
        searchable_text = " ".join([
            method.name,
            method.description,
            method.how_it_works,
            " ".join(method.pros),
            " ".join(method.cons),
            " ".join(method.best_for)
        ]).lower()
        
        if all(tag.lower() in searchable_text for tag in tags):
            results.append(method)
    
    return results


def get_crisis_resources() -> List[Resource]:
    """Get all crisis resources."""
    return [r for r in CRISIS_RESOURCES.values() if r.is_crisis_resource]


def get_all_resources() -> List[Resource]:
    """Get all resources including non-crisis resources."""
    return list(CRISIS_RESOURCES.values())


def get_resources_by_category(category: MethodCategory) -> List[Resource]:
    """Get resources for a specific category."""
    return [r for r in CRISIS_RESOURCES.values() if r.category == category]


def get_treatment_locators() -> List[Resource]:
    """Get treatment locator resources."""
    locator_keywords = ["locator", "finder", "find", "directory"]
    return [r for r in CRISIS_RESOURCES.values() 
            if any(kw in r.title.lower() or kw in r.description.lower() 
                   for kw in locator_keywords)]


def get_database_stats() -> Dict[str, any]:
    """Get statistics about the database."""
    methods = get_all_methods()
    
    # Category counts
    category_counts = {}
    for category in MethodCategory:
        count = len([m for m in methods if m.category == category])
        category_counts[category.value] = count
    
    # Evidence level counts
    evidence_counts = {}
    for level in EvidenceLevel:
        count = len([m for m in methods if m.evidence_level == level])
        evidence_counts[level.name] = count
    
    # Safety level counts
    safety_counts = {}
    for level in SafetyLevel:
        count = len([m for m in methods if m.safety_level == level])
        safety_counts[level.name] = count
    
    # Average effectiveness
    avg_effectiveness = sum(m.effectiveness_rating for m in methods) / len(methods) if methods else 0
    
    return {
        "total_methods": len(methods),
        "total_resources": len(CRISIS_RESOURCES),
        "crisis_resources": len(get_crisis_resources()),
        "category_counts": category_counts,
        "evidence_counts": evidence_counts,
        "safety_counts": safety_counts,
        "average_effectiveness": round(avg_effectiveness, 1),
        "categories_covered": len([c for c, count in category_counts.items() if count > 0])
    }


def get_quick_info(method_id: str) -> Optional[Dict[str, any]]:
    """Get quick summary information about a method for fast reference."""
    method = get_method_by_id(method_id)
    if not method:
        # Try synonym search
        results = search_methods(method_id)
        if results:
            method = results[0]
        else:
            return None
    
    return {
        "name": method.name,
        "category": method.category.value,
        "what_it_is": method.description[:200] + "..." if len(method.description) > 200 else method.description,
        "safety": method.safety_level.value,
        "effectiveness": f"{method.effectiveness_rating}/10",
        "evidence": method.evidence_level.value.split(" - ")[0],
        "cost": method.cost_range or "Varies",
        "key_pros": method.pros[:3] if method.pros else [],
        "key_risks": method.risks_side_effects[:3] if method.risks_side_effects else [],
        "where_to_find": method.where_to_find[:2] if method.where_to_find else [],
    }


def get_daily_quote() -> str:
    """Get a random daily motivation quote."""
    return random.choice(DAILY_QUOTES)


def get_coping_strategy() -> str:
    """Get a random coping strategy."""
    return random.choice(COPING_STRATEGIES)


def get_checkin_prompt() -> str:
    """Get a random check-in prompt."""
    return random.choice(CHECKIN_PROMPTS)


def get_multiple_coping_strategies(count: int = 5) -> List[str]:
    """Get multiple random coping strategies."""
    return random.sample(COPING_STRATEGIES, min(count, len(COPING_STRATEGIES)))


def calculate_sobriety_days(sobriety_date_str: str) -> Dict[str, int]:
    """
    Calculate days of sobriety from a date string.
    
    Args:
        sobriety_date_str: Date string in format YYYY-MM-DD
    
    Returns:
        Dictionary with days, weeks, months, and years
    """
    try:
        sobriety_date = datetime.strptime(sobriety_date_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format")
    
    today = date.today()
    
    if sobriety_date > today:
        raise ValueError("Sobriety date cannot be in the future")
    
    delta = today - sobriety_date
    total_days = delta.days
    
    # Use relativedelta for accurate year/month calculation accounting for leap years
    rd = relativedelta(today, sobriety_date)
    
    return {
        "total_days": total_days,
        "weeks": total_days // 7,
        "months": rd.years * 12 + rd.months,
        "years": rd.years,
        "days_in_current_week": total_days % 7,
        "milestone_message": _get_milestone_message(total_days)
    }


def _get_milestone_message(days: int) -> str:
    """Get an encouraging message based on sobriety milestone."""
    if days == 0:
        return "🌟 Day one is the first step of your journey. You've got this!"
    elif days == 1:
        return "⭐ One day! Every journey begins with a single step."
    elif days < 7:
        return f"💪 {days} days strong! Keep going, one day at a time."
    elif days == 7:
        return "🎉 ONE WEEK! This is a huge accomplishment!"
    elif days < 30:
        return f"🌟 {days} days! You're building something beautiful."
    elif days == 30:
        return "🎊 ONE MONTH! You're proving recovery is possible!"
    elif days < 60:
        return f"💫 {days} days! You're creating new habits and pathways."
    elif days == 60:
        return "🏆 TWO MONTHS! Your brain is healing every day."
    elif days == 90:
        return "🎯 90 DAYS! This is a major milestone in recovery!"
    elif days < 180:
        return f"🌈 {days} days! You're an inspiration."
    elif days == 180:
        return "🎉 SIX MONTHS! Half a year of freedom!"
    elif days < 365:
        return f"⭐ {days} days! Keep going, you're almost at a year!"
    elif days == 365:
        return "🏅 ONE YEAR! This is an incredible achievement!"
    elif days < 730:
        return f"👑 {days} days! Over a year of recovery!"
    elif days == 730:
        return "🎊 TWO YEARS! You're living proof that recovery works!"
    else:
        years = days // 365
        return f"🌟 {years}+ years! You're an inspiration to others in recovery!"


def export_method_to_text(method_id: str) -> str:
    """Export a method's information to a formatted text string."""
    method = get_method_by_id(method_id)
    if not method:
        raise ValueError(f"Method '{method_id}' not found")
    
    lines = [
        "=" * 60,
        f"  {method.name}",
        "=" * 60,
        "",
        f"Category: {method.category.value}",
        "",
        "DESCRIPTION",
        "-" * 40,
        method.description,
        "",
        "HOW IT WORKS",
        "-" * 40,
        method.how_it_works,
        "",
        "KEY INFORMATION",
        "-" * 40,
        f"Evidence Level: {method.evidence_level.value}",
        f"Safety Level: {method.safety_level.value}",
        f"Effectiveness Rating: {method.effectiveness_rating}/10",
        f"Accessibility: {method.accessibility.value}",
    ]
    
    if method.typical_duration:
        lines.append(f"Typical Duration: {method.typical_duration}")
    if method.cost_range:
        lines.append(f"Cost Range: {method.cost_range}")
    if method.insurance_coverage:
        lines.append(f"Insurance Coverage: {method.insurance_coverage}")
    if method.success_rate:
        lines.append(f"Success Rate: {method.success_rate}")
    
    if method.pros:
        lines.extend(["", "PROS", "-" * 40])
        lines.extend([f"• {pro}" for pro in method.pros])
    
    if method.cons:
        lines.extend(["", "CONS", "-" * 40])
        lines.extend([f"• {con}" for con in method.cons])
    
    if method.risks_side_effects:
        lines.extend(["", "RISKS AND SIDE EFFECTS", "-" * 40])
        lines.extend([f"• {risk}" for risk in method.risks_side_effects])
    
    if method.contraindications:
        lines.extend(["", "CONTRAINDICATIONS", "-" * 40])
        lines.extend([f"• {contra}" for contra in method.contraindications])
    
    if method.best_for:
        lines.extend(["", "BEST FOR", "-" * 40])
        lines.extend([f"• {item}" for item in method.best_for])
    
    if method.not_recommended_for:
        lines.extend(["", "NOT RECOMMENDED FOR", "-" * 40])
        lines.extend([f"• {item}" for item in method.not_recommended_for])
    
    if method.where_to_find:
        lines.extend(["", "WHERE TO FIND", "-" * 40])
        lines.extend([f"• {loc}" for loc in method.where_to_find])
    
    if method.resources:
        lines.extend(["", "RESOURCES", "-" * 40])
        lines.extend([f"• {res}" for res in method.resources])
    
    lines.extend([
        "",
        "=" * 60,
        "DISCLAIMER: This information is for educational purposes only.",
        "Always consult healthcare providers for medical advice.",
        "=" * 60
    ])
    
    return "\n".join(lines)


def export_crisis_card() -> str:
    """Export a printable crisis card with emergency resources."""
    crisis = get_crisis_resources()
    
    lines = [
        "╔" + "═" * 58 + "╗",
        "║" + " CRISIS RESOURCES - KEEP THIS CARD ".center(58) + "║",
        "╠" + "═" * 58 + "╣",
        "║" + " ".center(58) + "║",
        "║" + " 🆘 EMERGENCIES: Call 911 ".center(58) + "║",
        "║" + " ".center(58) + "║",
    ]
    
    for resource in crisis[:10]:  # Limit to 10 for card size
        phone_line = resource.phone if resource.phone else resource.url
        if phone_line:
            title_trunc = resource.title[:25] + "..." if len(resource.title) > 28 else resource.title
            phone_trunc = phone_line[:25] if len(phone_line) > 25 else phone_line
            line = f" {title_trunc}: {phone_trunc}"
            lines.append("║" + line.ljust(58) + "║")
    
    lines.extend([
        "║" + " ".center(58) + "║",
        "║" + " 💙 Recovery is possible. You are not alone. 💙 ".center(58) + "║",
        "║" + " ".center(58) + "║",
        "╚" + "═" * 58 + "╝"
    ])
    
    return "\n".join(lines)