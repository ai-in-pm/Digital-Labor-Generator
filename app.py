from flask import Flask, request, jsonify
from flask_cors import CORS
from digital_labor import DigitalLaborCalculator, HumanEmployee
from datetime import datetime

app = Flask(__name__)
CORS(app)

calculator = DigitalLaborCalculator()

@app.route('/api/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        human_data = data.get('human', {})
        ai_data = data.get('ai_agent', {})
        metrics = data.get('metrics', {})

        # Convert contract_date string to datetime if present
        if human_data.get('contract_date'):
            human_data['contract_date'] = datetime.fromisoformat(human_data['contract_date'])

        # Create HumanEmployee instance
        human = HumanEmployee(**human_data)

        # Calculate results
        results = calculator.calculate_wages_and_costs({
            'human': human,
            'ai_agent': ai_data,
            'metrics': metrics
        })

        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
