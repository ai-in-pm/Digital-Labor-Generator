# Digital Labor Generator App

A comprehensive application for calculating and managing costs associated with human-AI collaboration, ensuring compliance with Fair Labor Standards Act (FLSA), Service Contract Act (SCA), and Davis-Bacon Act regulations.

This GitHub Repository is only for Research purposes only, it is not intended to be used as guidance, requirements, and or confirmation of Digital Labor to AI Agents.

## Features

### Cost Calculation and Management
- Calculate human wages based on role, hours, and complexity
- Compute AI operational costs based on usage and performance metrics
- Generate wage adjustment recommendations based on AI integration
- Analyze cost-to-value ratios for human-AI collaboration

### Federal Labor Law Compliance
- Service Contract Act (SCA) Wage Determinations
  - Occupation-specific wage rates (WD 2015-5623 Rev 25)
  - Health & Welfare benefits ($5.36/hour standard rate)
  - Vacation benefits (2-5 weeks based on years of service)
  - 11 paid holidays per year
  - Sick leave under Executive Order 13706

- Davis-Bacon Act Wage Determinations
  - Construction-specific wage rates
  - Fringe benefits calculations
  - Local area wage determinations

- Executive Order Compliance
  - EO 14026: $17.75 minimum wage (2025)
  - EO 13658: $13.30 minimum wage (2025)
  - EO 13706: Paid sick leave requirements

### User Interface
- Modern Material Design interface
- Responsive layout for all devices
- Real-time form validation
- Interactive input fields
- Beautiful results display with cards
- Loading states and error handling

## Requirements

- Python 3.8+
- Required packages (see requirements.txt):
  - pydantic>=2.5.0
  - pandas>=2.0.0
  - numpy>=1.24.0
  - flask>=3.0.0
  - flask-cors>=4.0.0
  - python-dotenv>=1.0.0

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

1. Start the Flask backend:
```bash
python app.py
```

2. Open `static/index.html` in your web browser

### Using the Interface

1. Fill in the Human Employee Information:
   - Role and basic information
   - Contract type (SCA or Davis-Bacon)
   - Occupation code from wage determination
   - Years of service (for SCA)

2. Enter AI Agent Details:
   - Model selection
   - Query volume and complexity
   - Infrastructure costs

3. Specify Collaboration Metrics:
   - Human-AI collaboration ratio
   - Expected business value

4. Click "Calculate" to get results including:
   - Detailed wage breakdown
   - AI operational costs
   - Wage recommendations
   - Cost-to-value analysis

### API Usage

```python
from digital_labor import DigitalLaborCalculator

# Initialize calculator
calculator = DigitalLaborCalculator()

# Calculate wages and costs
data = {
    "human": {
        "role": "IT Support",
        "hours_worked": 40,
        "hourly_wage": 38.58,
        "task_complexity": 3,
        "occupation_code": "14160",  # Personal Computer Support Technician
        "is_service_contract": True,
        "years_of_service": 5,
        "has_eo13706": True
    },
    "ai_agent": {
        "model": "GPT-4",
        "total_queries": 5000,
        "query_complexity": 3,
        "infrastructure_cost": 150
    },
    "metrics": {
        "collaboration_ratio": 0.7,
        "business_value": 20000
    }
}

results = calculator.calculate_wages_and_costs(data)
```

## Input Data Format

### Human Employee Data
- `role`: Job title or role description
- `hours_worked`: Number of hours worked
- `hourly_wage`: Base hourly wage rate
- `task_complexity`: Scale of 1-5
- `occupation_code`: SCA or Davis-Bacon occupation code
- `is_service_contract`: Boolean for SCA vs Davis-Bacon
- `years_of_service`: Years with contractor (for SCA)
- `has_eo13706`: Boolean for EO 13706 compliance

### AI Agent Data
- `model`: AI model specification
- `total_queries`: Number of queries processed
- `query_complexity`: Scale of 1-5
- `infrastructure_cost`: Operational costs

### Collaboration Metrics
- `collaboration_ratio`: Human-AI workload split
- `business_value`: Value generated from collaboration

## Output Format

```python
{
    "human_wages": {
        "base_pay": 1543.20,
        "health_welfare": 214.40,
        "vacation_pay": 118.71,
        "holiday_pay": 65.29,
        "total_compensation": 1941.60
    },
    "ai_costs": 200.00,
    "collaboration_metrics": {
        "total_cost": 2141.60,
        "cost_to_value_ratio": 0.107
    },
    "wage_recommendations": {
        "action": "Increase",
        "adjustment_percentage": 10.0,
        "reason": "Effective AI collaboration with moderate complexity"
    }
}

## Useful Resources

### Federal Wage Determinations
- [Davis-Bacon Act Wage Determinations](https://sam.gov/search/?index=dbra&page=1&pageSize=25&sort=-modifiedDate&sfm%5Bstatus%5D%5Bis_active%5D=true) - Search active Davis-Bacon wage determinations
- [Service Contract Act Directory](https://sam.gov/search/?index=sca&page=1&pageSize=25&sort=-modifiedDate&sfm%5Bstatus%5D%5Bis_active%5D=true) - Search active SCA wage determinations
- [FLSA Digital Reference Guide](https://www.dol.gov/sites/dolgov/files/WHD/legacy/files/Digital_Reference_Guide_FLSA.pdf) - Department of Labor's guide to FLSA compliance
- [SAM.gov Help Guide](https://www.fsd.gov/gsafsd_sp?id=gsa_kb_view2&kb_id=f66d8e6cdb76d4100d73f81d0f9619c6) - How to find and download wage determinations

These resources are regularly updated by the Department of Labor and SAM.gov. Always refer to the latest wage determinations when calculating wages and benefits.

## Project Structure

```
Digital_Labor/
├── app.py                    # Flask backend server
├── digital_labor.py          # Main calculator logic
├── wage_determination.py     # Davis-Bacon wage calculations
├── sca_wage_determination.py # SCA wage calculations
├── requirements.txt          # Python dependencies
├── static/                   # Frontend files
│   ├── index.html           # Main HTML file
│   ├── styles.css           # Custom styles
│   └── app.js               # React application
└── test_calculator.py        # Test suite
