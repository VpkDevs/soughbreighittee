"""
Database of recovery methods for opiate addiction.

This module contains a comprehensive collection of all known recovery methods
for Opiate Use Disorder, including both evidence-based and alternative approaches.
"""

from typing import Dict, List
from .models import RecoveryMethod, MethodCategory, EvidenceLevel, SafetyLevel, AccessibilityLevel, Resource


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
}


def get_all_methods() -> List[RecoveryMethod]:
    """Get all recovery methods."""
    return list(RECOVERY_METHODS_DB.values())


def get_methods_by_category(category: MethodCategory) -> List[RecoveryMethod]:
    """Get all methods in a specific category."""
    return [method for method in RECOVERY_METHODS_DB.values() 
            if method.category == category]


def get_method_by_id(method_id: str) -> RecoveryMethod:
    """Get a specific method by ID."""
    if method_id not in RECOVERY_METHODS_DB:
        raise ValueError(f"Method with ID '{method_id}' not found")
    return RECOVERY_METHODS_DB[method_id]


def search_methods(query: str) -> List[RecoveryMethod]:
    """Search methods by name, description, or keywords."""
    query = query.lower()
    results = []
    
    for method in RECOVERY_METHODS_DB.values():
        if (query in method.name.lower() or 
            query in method.description.lower() or
            any(query in keyword.lower() for keyword in method.pros + method.cons)):
            results.append(method)
    
    return results


def get_crisis_resources() -> List[Resource]:
    """Get all crisis resources."""
    return list(CRISIS_RESOURCES.values())