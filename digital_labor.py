from typing import Dict, List, Optional
from pydantic import BaseModel, Field
import numpy as np

class HumanEmployee(BaseModel):
    role: str
    hours_worked: float
    hourly_wage: float
    task_complexity: int = Field(ge=1, le=5)

class AIAgent(BaseModel):
    model: str
    total_queries: int
    query_complexity: int = Field(ge=1, le=5)
    infrastructure_cost: float
    accuracy: Optional[float] = None
    latency: Optional[float] = None

class CollaborationMetrics(BaseModel):
    collaboration_ratio: float = Field(ge=0, le=1)
    business_value: float

class DigitalLaborCalculator:
    FEDERAL_MINIMUM_WAGE = 7.25
    STATE_MINIMUM_WAGE = 10.00  # Example state-specific value
    MINIMUM_WAGE = max(FEDERAL_MINIMUM_WAGE, STATE_MINIMUM_WAGE)
    AI_BASE_COST = 0.01
    HUMAN_TASK_WEIGHT = 0.7
    AI_TASK_WEIGHT = 0.3

    def calculate_human_wages(self, employee: HumanEmployee) -> float:
        """Calculate human wages ensuring compliance with minimum wage laws."""
        hourly_wage = max(employee.hourly_wage, self.MINIMUM_WAGE)
        complexity_multiplier = 1 + (0.1 * (employee.task_complexity - 1))
        return hourly_wage * employee.hours_worked * complexity_multiplier

    def calculate_ai_costs(self, ai_agent: AIAgent) -> float:
        """Calculate AI operational costs based on usage and complexity."""
        base_cost = self.AI_BASE_COST * ai_agent.total_queries
        complexity_cost = ai_agent.infrastructure_cost * ai_agent.query_complexity
        return base_cost + complexity_cost

    def calculate_collaboration_cost(
        self, human_wages: float, ai_cost: float, metrics: CollaborationMetrics
    ) -> Dict:
        """Calculate total collaboration cost and cost-to-value ratio."""
        weighted_human_cost = self.HUMAN_TASK_WEIGHT * human_wages
        weighted_ai_cost = self.AI_TASK_WEIGHT * ai_cost
        total_cost = weighted_human_cost + weighted_ai_cost
        
        cost_to_value = (
            total_cost / metrics.business_value if metrics.business_value > 0 else 0
        )
        
        return {
            "total_cost": round(total_cost, 2),
            "cost_to_value_ratio": round(cost_to_value, 4)
        }

    def recommend_wage_adjustments(
        self, employee: HumanEmployee, metrics: CollaborationMetrics
    ) -> Dict:
        """Generate wage adjustment recommendations based on AI collaboration."""
        base_recommendation = {
            "adjustment_percentage": 0.0,
            "reason": "",
            "action": ""
        }

        # High complexity tasks with good business value
        if employee.task_complexity >= 4 and metrics.business_value > 0:
            base_recommendation.update({
                "adjustment_percentage": 15.0,
                "reason": "High complexity tasks with proven business value",
                "action": "Increase"
            })
        # High AI collaboration with moderate complexity
        elif metrics.collaboration_ratio > 0.7 and employee.task_complexity >= 3:
            base_recommendation.update({
                "adjustment_percentage": 10.0,
                "reason": "Effective AI collaboration with moderate complexity",
                "action": "Increase"
            })
        # Low complexity with high AI automation
        elif employee.task_complexity <= 2 and metrics.collaboration_ratio > 0.8:
            base_recommendation.update({
                "adjustment_percentage": -5.0,
                "reason": "Reduced complexity due to AI automation",
                "action": "Decrease"
            })
        else:
            base_recommendation.update({
                "adjustment_percentage": 0.0,
                "reason": "Current wage level appropriate",
                "action": "Maintain"
            })

        return base_recommendation

    def calculate_wages_and_costs(self, data: Dict) -> Dict:
        """Calculate all metrics and generate recommendations."""
        employee = HumanEmployee(**data["human"])
        ai_agent = AIAgent(**data["ai_agent"])
        metrics = CollaborationMetrics(**data["metrics"])

        human_wages = self.calculate_human_wages(employee)
        ai_costs = self.calculate_ai_costs(ai_agent)
        collaboration_metrics = self.calculate_collaboration_cost(
            human_wages, ai_costs, metrics
        )
        recommendations = self.recommend_wage_adjustments(employee, metrics)

        return {
            "human_wages": round(human_wages, 2),
            "ai_costs": round(ai_costs, 2),
            "collaboration_metrics": collaboration_metrics,
            "wage_recommendations": recommendations
        }
