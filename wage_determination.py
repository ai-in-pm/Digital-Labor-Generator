from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime
from pydantic import BaseModel

class WageRate(BaseModel):
    occupation: str
    base_rate: float
    fringe_benefits: float
    total_rate: float

class DavisBaconWageDetermination:
    EXECUTIVE_ORDER_14026_MIN_WAGE = 17.75  # 2025 rate
    EXECUTIVE_ORDER_13658_MIN_WAGE = 13.30  # 2025 rate

    def __init__(self):
        self.wage_rates = self._initialize_wage_rates()

    def _initialize_wage_rates(self) -> Dict[str, WageRate]:
        """Initialize wage rates from the determination CA20250001."""
        return {
            "ASBESTOS_WORKER": WageRate(
                occupation="Asbestos Workers/Insulator",
                base_rate=49.58,
                fringe_benefits=25.27,
                total_rate=74.85
            ),
            "ELECTRICIAN": WageRate(
                occupation="Electrician",
                base_rate=52.85,
                fringe_benefits=17.62,
                total_rate=70.47
            ),
            "ELEVATOR_MECHANIC": WageRate(
                occupation="Elevator Mechanic",
                base_rate=66.63,
                fringe_benefits=37.885,
                total_rate=104.515
            ),
            "LABORER_BASIC": WageRate(
                occupation="Laborer Group 1",
                base_rate=37.68,
                fringe_benefits=22.44,
                total_rate=60.12
            )
        }

    def get_minimum_wage(self, contract_date: datetime) -> float:
        """Determine minimum wage based on contract date."""
        if contract_date >= datetime(2022, 1, 30):
            return self.EXECUTIVE_ORDER_14026_MIN_WAGE
        return self.EXECUTIVE_ORDER_13658_MIN_WAGE

    def get_wage_rate(self, occupation: str) -> Optional[WageRate]:
        """Get wage rate for a specific occupation."""
        return self.wage_rates.get(occupation.upper())

    def calculate_total_compensation(self, occupation: str, hours: float) -> Dict:
        """Calculate total compensation including base rate and fringe benefits."""
        wage_rate = self.get_wage_rate(occupation)
        if not wage_rate:
            return {
                "error": f"Occupation {occupation} not found in wage determination"
            }

        return {
            "occupation": wage_rate.occupation,
            "hours": hours,
            "base_pay": round(wage_rate.base_rate * hours, 2),
            "fringe_benefits": round(wage_rate.fringe_benefits * hours, 2),
            "total_compensation": round(wage_rate.total_rate * hours, 2)
        }
