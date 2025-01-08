from typing import Dict, Optional
from dataclasses import dataclass
from datetime import datetime
from pydantic import BaseModel

class SCAWageRate(BaseModel):
    occupation_code: str
    title: str
    base_rate: float
    health_welfare: float = 5.36  # Default H&W rate per hour
    health_welfare_eo13706: float = 4.93  # H&W rate for contracts with EO 13706

class SCABenefits(BaseModel):
    vacation_weeks: int
    paid_holidays: int = 11
    sick_leave_hours: int = 56  # EO 13706: 1 hour per 30 hours worked, up to 56 hours

class SCAWageDetermination:
    """Handles Service Contract Act wage determinations (WD 2015-5623 Rev 25)"""
    
    EXEC_ORDER_14026_MIN_WAGE = 17.75  # 2025 rate
    EXEC_ORDER_13658_MIN_WAGE = 13.30  # 2025 rate
    
    def __init__(self):
        self.wage_rates = self._initialize_wage_rates()
        
    def _initialize_wage_rates(self) -> Dict[str, SCAWageRate]:
        """Initialize wage rates from WD 2015-5623 Rev 25."""
        return {
            "01020": SCAWageRate(
                occupation_code="01020",
                title="Administrative Assistant",
                base_rate=46.70
            ),
            "14044": SCAWageRate(
                occupation_code="14044",
                title="Computer Operator IV",
                base_rate=38.58
            ),
            "14160": SCAWageRate(
                occupation_code="14160",
                title="Personal Computer Support Technician",
                base_rate=38.58
            ),
            "14170": SCAWageRate(
                occupation_code="14170",
                title="System Support Specialist",
                base_rate=43.12
            ),
            "30086": SCAWageRate(
                occupation_code="30086",
                title="Engineering Technician VI",
                base_rate=47.80
            )
        }

    def calculate_benefits(self, years_of_service: int) -> SCABenefits:
        """Calculate vacation weeks based on years of service."""
        if years_of_service >= 25:
            vacation_weeks = 5
        elif years_of_service >= 15:
            vacation_weeks = 4
        elif years_of_service >= 5:
            vacation_weeks = 3
        else:
            vacation_weeks = 2
            
        return SCABenefits(vacation_weeks=vacation_weeks)

    def get_wage_rate(self, occupation_code: str) -> Optional[SCAWageRate]:
        """Get wage rate for a specific occupation code."""
        return self.wage_rates.get(occupation_code)

    def calculate_total_compensation(
        self, 
        occupation_code: str, 
        hours: float,
        years_of_service: int,
        has_eo13706: bool = False
    ) -> Dict:
        """Calculate total compensation including wages and benefits."""
        wage_rate = self.get_wage_rate(occupation_code)
        if not wage_rate:
            return {
                "error": f"Occupation code {occupation_code} not found"
            }

        # Calculate base compensation
        base_pay = wage_rate.base_rate * hours

        # Calculate health and welfare
        hw_rate = wage_rate.health_welfare_eo13706 if has_eo13706 else wage_rate.health_welfare
        hw_pay = min(hw_rate * hours, hw_rate * 40)  # Cap at 40 hours per week

        # Calculate vacation and holiday pay
        benefits = self.calculate_benefits(years_of_service)
        vacation_hours = benefits.vacation_weeks * 40
        holiday_hours = benefits.paid_holidays * 8
        vacation_pay = (wage_rate.base_rate * vacation_hours) / 52  # Weekly proration
        holiday_pay = (wage_rate.base_rate * holiday_hours) / 52   # Weekly proration

        return {
            "occupation": wage_rate.title,
            "base_pay": round(base_pay, 2),
            "health_welfare": round(hw_pay, 2),
            "vacation_pay": round(vacation_pay, 2),
            "holiday_pay": round(holiday_pay, 2),
            "total_compensation": round(base_pay + hw_pay + vacation_pay + holiday_pay, 2),
            "benefits": {
                "vacation_weeks": benefits.vacation_weeks,
                "paid_holidays": benefits.paid_holidays,
                "sick_leave_hours": benefits.sick_leave_hours if has_eo13706 else 0
            }
        }
