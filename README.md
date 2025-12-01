# Soughbreighittee - Comprehensive Harm Reduction and Addiction Recovery App

A comprehensive tool for exploring recovery methods for Opiate Use Disorder (OUD), providing detailed information and comparison of all known recovery approaches with a focus on harm reduction.

## ⚠️ MEDICAL DISCLAIMER

**THIS APPLICATION IS FOR INFORMATIONAL PURPOSES ONLY** and should not replace professional medical advice, diagnosis, or treatment. Always seek the advice of qualified healthcare providers regarding any medical condition or treatment options. If you are experiencing a medical emergency, call 911 immediately.

The creators of this application are not medical professionals and do not endorse any specific treatment methods. Users are encouraged to work with healthcare providers to develop appropriate treatment plans.

## 🆘 Emergency Contacts

- **National Suicide Prevention Lifeline**: 988
- **SAMHSA National Helpline**: 1-800-662-4357  
- **Crisis Text Line**: Text HOME to 741741
- **Veterans Crisis Line**: 988, then press 1
- **Poison Control**: 1-800-222-1222

## 🎯 Purpose

This application aims to be the most comprehensive, harm-reduction focused addiction recovery method compendium ever built for Opiate Use Disorder. It details all possible information and dimensions of comparison for all known recovery methods, both legal and illicit, both wise and foolish, both effective and useless - if someone out there is trying the method, it's included and fully detailed.

## 📋 Features

### Core Features
- **Comprehensive Database**: 36+ recovery methods across all categories
- **Evidence-Based Information**: Each method includes evidence level, effectiveness rating, and safety information
- **Harm Reduction Focus**: Includes both abstinence-based and harm reduction approaches
- **Interactive Exploration**: Guided tools to help find methods that match your situation
- **Comparison Tools**: Side-by-side comparison of different recovery approaches
- **Crisis Resources**: 15+ crisis resources including international and specialized hotlines

### New in v0.2.0
- **Daily Recovery Tools**: Motivation quotes, coping strategies, check-in prompts
- **Sobriety Calculator**: Track your recovery journey with milestone messages
- **Quick Info Command**: Get key facts about any method instantly
- **Enhanced Search**: Synonym matching (e.g., "suboxone" finds "buprenorphine")
- **Export Features**: Export method info and printable crisis cards
- **Database Statistics**: View comprehensive database overview
- **Expanded Resources**: Treatment locators, international hotlines, specialized support

## 🏥 Recovery Method Categories

| Category | Methods | Description |
|----------|---------|-------------|
| **Medical-Assisted Treatment (MAT)** | 8 | FDA-approved medications like methadone, buprenorphine, naltrexone, Sublocade |
| **Behavioral Therapy** | 8 | CBT, DBT, MET, motivational interviewing, group therapy, family therapy |
| **Support Groups** | 3 | NA, SMART Recovery, Al-Anon/Nar-Anon for families |
| **Harm Reduction** | 6 | Naloxone, needle exchange, fentanyl test strips, safe consumption sites |
| **Peer Support** | 4 | Recovery coaching, peer support specialists, sober living, recovery community centers |
| **Alternative/Complementary** | 4 | Acupuncture, kratom, ibogaine, recovery apps |
| **Crisis/Emergency** | 2 | Crisis hotlines, professional intervention |
| **Holistic Wellness** | 1 | Yoga and meditation |

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/VpkDevs/soughbreighittee.git
cd soughbreighittee
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

Or install as a package:
```bash
pip install -e .
soughbreighittee --help
```

## 💻 Usage

### Quick Start
```bash
python main.py                    # Show help and available commands
python main.py interactive        # Guided exploration (recommended)
python main.py list               # List all methods
python main.py emergency          # Crisis resources
```

### Search for Methods
```bash
python main.py search methadone       # Direct search
python main.py search suboxone        # Synonym search (finds buprenorphine)
python main.py search therapy         # Category search
```

### View Method Information
```bash
python main.py show naloxone          # Full detailed view
python main.py quick naloxone         # Quick key facts
python main.py show buprenorphine     # View another method
```

### Daily Recovery Tools
```bash
python main.py daily                  # All daily tools at once
python main.py motivation             # Daily motivation quote
python main.py cope                   # Coping strategies
python main.py checkin               # Reflection prompts
python main.py sobriety 2024-01-15   # Calculate sobriety time
```

### Compare Methods
```bash
python main.py compare                # Interactive comparison tool
```

### Filter Methods
```bash
python main.py list --category MEDICAL_ASSISTED_TREATMENT
python main.py list --evidence HIGH --min-effectiveness 7
python main.py list --safety SAFE
python main.py categories             # View all categories with counts
```

### Resources & Statistics
```bash
python main.py emergency              # Crisis resources
python main.py resources              # All resources (locators, organizations)
python main.py stats                  # Database statistics
```

### Export Features
```bash
python main.py export naloxone                    # Print to console
python main.py export naloxone -o naloxone.txt    # Save to file
python main.py crisis-card                        # Printable crisis card
python main.py crisis-card -o card.txt            # Save crisis card to file
```

## 📊 Method Information Included

For each recovery method, the app provides:

- **Basic Information**: Description, how it works, typical duration
- **Evidence & Effectiveness**: Scientific evidence level, effectiveness rating (1-10), success rates
- **Safety Profile**: Safety level, risks, side effects, contraindications (with color-coded warnings)
- **Practical Details**: Cost, insurance coverage, accessibility, requirements
- **Suitability**: Who it works best for, who should avoid it
- **Logistics**: Where to find it, what's required to access it
- **Interactions**: What it can/cannot be combined with
- **Resources**: Additional information sources and contacts

## 🔍 Smart Search Features

The search now includes:
- **Synonym Matching**: "suboxone", "subutex", "bupe" all find buprenorphine
- **Medication Names**: "narcan", "vivitrol", "evzio" find their generic equivalents
- **Fuzzy Matching**: Partial matches and typos are handled
- **Tag-Based Search**: Search across all method attributes

## 🆘 Crisis Resources

The app includes 15+ crisis resources:
- **National Hotlines**: 988, SAMHSA, Crisis Text Line
- **Specialized Support**: Veterans, LGBTQ+, Trans, Youth, Teen
- **International**: Canada, UK, Australia, plus global directories
- **Treatment Locators**: SAMHSA, buprenorphine providers, NA/SMART meetings
- **Educational**: NIDA, Harm Reduction Coalition, Faces & Voices of Recovery

## 🎯 Coverage Philosophy

This app takes a comprehensive, non-judgmental approach to recovery information:

- **Evidence-Based Methods**: FDA-approved medications, proven therapies
- **Harm Reduction**: Approaches that reduce risks without requiring abstinence
- **Alternative Approaches**: Complementary and alternative medicine options
- **Experimental Methods**: Treatments under research or with limited evidence
- **Controversial Methods**: Approaches with mixed or disputed evidence
- **All Risk Levels**: From completely safe to high-risk approaches (with clear warnings)

The goal is informed choice - providing complete information so individuals and healthcare providers can make educated decisions about treatment approaches.

## 🛡️ Safety Philosophy

- **Complete Information**: Both benefits and risks are clearly presented
- **Risk Assessment**: Each method has a clear safety rating with color coding
- **Medical Supervision**: Emphasis on working with healthcare providers
- **Harm Reduction**: Recognition that any movement toward safer use is positive
- **Crisis Resources**: Always available emergency contacts and resources
- **High-Risk Warnings**: Prominent warnings for dangerous methods

## 🧪 Testing

Run the test suite:
```bash
python -m pytest tests/ -v
```

All 39 tests cover:
- Basic functionality
- New recovery methods and categories
- Search functionality (including synonyms)
- Daily tools and helper functions
- Export features
- Resource availability

## 🤝 Contributing

This project aims to be the most comprehensive resource available. Contributions are welcome:

- **Method Information**: Additional recovery methods or updated information
- **Evidence Updates**: New research or clinical data
- **Resource Links**: Treatment centers, support organizations, educational materials
- **Translation**: Making the app available in other languages
- **Accessibility**: Improving usability for different populations

## 📜 License

This project is released into the public domain under The Unlicense. See the LICENSE file for details.

## 🙏 Acknowledgments

This project is dedicated to everyone affected by the opioid crisis - those in recovery, those still struggling, their families and loved ones, healthcare providers, harm reduction workers, and advocates working to save lives and reduce suffering.

**Recovery is possible. Help is available. Every life has value.**

---

*If you or someone you know is struggling, please reach out:*
- **988** - Suicide & Crisis Lifeline
- **1-800-662-4357** - SAMHSA National Helpline
- **Text HOME to 741741** - Crisis Text Line
