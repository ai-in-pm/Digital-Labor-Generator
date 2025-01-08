from digital_labor import DigitalLaborCalculator

def main():
    # Sample input data
    data = {
        "human": {
            "role": "AI Supervisor",
            "hours_worked": 40,
            "hourly_wage": 15.00,
            "task_complexity": 4
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

    # Initialize calculator
    calculator = DigitalLaborCalculator()

    # Calculate results
    results = calculator.calculate_wages_and_costs(data)

    # Print results
    print("\nDigital Labor Cost Analysis")
    print("==========================")
    print(f"Human Wages: ${results['human_wages']}")
    print(f"AI Costs: ${results['ai_costs']}")
    print(f"\nCollaboration Metrics:")
    print(f"Total Cost: ${results['collaboration_metrics']['total_cost']}")
    print(f"Cost-to-Value Ratio: {results['collaboration_metrics']['cost_to_value_ratio']}")
    print(f"\nWage Recommendations:")
    print(f"Action: {results['wage_recommendations']['action']}")
    print(f"Adjustment: {results['wage_recommendations']['adjustment_percentage']}%")
    print(f"Reason: {results['wage_recommendations']['reason']}")

if __name__ == "__main__":
    main()
