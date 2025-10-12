# Soughbreighittee - Comprehensive Harm Reduction and Addiction Recovery App

[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code style: PEP 8](https://img.shields.io/badge/code%20style-PEP%208-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

A comprehensive tool for exploring recovery methods for Opiate Use Disorder (OUD), providing detailed information and comparison of all known recovery approaches with a focus on harm reduction.

---

## ⚠️ MEDICAL DISCLAIMER

**THIS APPLICATION IS FOR INFORMATIONAL PURPOSES ONLY** and should not replace professional medical advice, diagnosis, or treatment. Always seek the advice of qualified healthcare providers regarding any medical condition or treatment options. If you are experiencing a medical emergency, call 911 immediately.

The creators of this application are not medical professionals and do not endorse any specific treatment methods. Users are encouraged to work with healthcare providers to develop appropriate treatment plans.

## 🆘 Emergency Contacts

- **National Suicide Prevention Lifeline**: 988
- **SAMHSA National Helpline**: 1-800-662-4357  
- **Crisis Text Line**: Text HOME to 741741
- **National Overdose Prevention Network**: https://www.overdoselifeline.org/

## 🎯 Purpose

This application aims to be the most comprehensive, harm-reduction focused addiction recovery method compendium ever built for Opiate Use Disorder. It details all possible information and dimensions of comparison for all known recovery methods, both legal and illicit, both wise and foolish, both effective and useless - if someone out there is trying the method, it's included and fully detailed.

## 📋 Features

- **Comprehensive Database**: Detailed information on dozens of recovery methods
- **Evidence-Based Information**: Each method includes evidence level, effectiveness rating, and safety information
- **Harm Reduction Focus**: Includes both abstinence-based and harm reduction approaches
- **Interactive Exploration**: Guided tools to help find methods that match your situation
- **Comparison Tools**: Side-by-side comparison of different recovery approaches
- **Crisis Resources**: Quick access to emergency contacts and crisis support

## 🏥 Recovery Method Categories

- **Medical-Assisted Treatment (MAT)**: FDA-approved medications like methadone, buprenorphine, naltrexone
- **Behavioral Therapy**: CBT, contingency management, motivational interviewing
- **Support Groups**: NA, SMART Recovery, refuge recovery
- **Harm Reduction**: Needle exchange, naloxone, safe consumption sites
- **Alternative/Complementary**: Acupuncture, yoga, meditation, kratom, ibogaine
- **Crisis/Emergency**: Hotlines, emergency services, overdose prevention
- **Holistic Wellness**: Mind-body approaches, nutrition, exercise
- **Peer Support**: Recovery coaching, mentorship programs

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

### Interactive Mode (Recommended for first-time users)
```bash
python main.py interactive
```

### List all methods
```bash
python main.py list
```

### Search for methods
```bash
python main.py search methadone
python main.py search therapy
python main.py search harm reduction
```

### View detailed information about a method
```bash
python main.py show methadone
python main.py show naloxone
```

### Compare methods
```bash
python main.py compare
```

### View by category
```bash
python main.py list --category MEDICAL_ASSISTED_TREATMENT
python main.py list --category HARM_REDUCTION
```

### Filter by evidence level or safety
```bash
python main.py list --evidence HIGH --min-effectiveness 7
python main.py list --safety SAFE
```

### Emergency resources
```bash
python main.py emergency
```

## 📊 Method Information Included

For each recovery method, the app provides:

- **Basic Information**: Description, how it works, typical duration
- **Evidence & Effectiveness**: Scientific evidence level, effectiveness rating (1-10), success rates
- **Safety Profile**: Safety level, risks, side effects, contraindications
- **Practical Details**: Cost, insurance coverage, accessibility, requirements
- **Suitability**: Who it works best for, who should avoid it
- **Logistics**: Where to find it, what's required to access it
- **Interactions**: What it can/cannot be combined with
- **Resources**: Additional information sources and contacts

## 🎯 Coverage Philosophy

This app takes a comprehensive, non-judgmental approach to recovery information:

- **Evidence-Based Methods**: FDA-approved medications, proven therapies
- **Harm Reduction**: Approaches that reduce risks without requiring abstinence
- **Alternative Approaches**: Complementary and alternative medicine options
- **Experimental Methods**: Treatments under research or with limited evidence
- **Controversial Methods**: Approaches with mixed or disputed evidence
- **All Risk Levels**: From completely safe to high-risk approaches

The goal is informed choice - providing complete information so individuals and healthcare providers can make educated decisions about treatment approaches.

## 🛡️ Safety Philosophy

- **Complete Information**: Both benefits and risks are clearly presented
- **Risk Assessment**: Each method has a clear safety rating
- **Medical Supervision**: Emphasis on working with healthcare providers
- **Harm Reduction**: Recognition that any movement toward safer use is positive
- **Crisis Resources**: Always available emergency contacts and resources

## 🤝 Contributing

This project aims to be the most comprehensive resource available. Contributions are welcome!

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines on:
- Adding or updating recovery methods
- Code contributions and style guidelines
- Testing requirements
- Sensitive content considerations

Quick contribution areas:
- **Method Information**: Additional recovery methods or updated information
- **Evidence Updates**: New research or clinical data
- **Resource Links**: Treatment centers, support organizations, educational materials
- **Translation**: Making the app available in other languages
- **Accessibility**: Improving usability for different populations

## 📜 License

This project is released into the public domain under The Unlicense. See the LICENSE file for details.

## 🙏 Acknowledgments

This project is dedicated to everyone affected by the opioid crisis - those in recovery, those still struggling, their families and loved ones, healthcare providers, harm reduction workers, and advocates working to save lives and reduce suffering.

Recovery is possible. Help is available. Every life has value.
