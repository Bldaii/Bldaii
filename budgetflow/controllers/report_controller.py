from datetime import date, datetime
import calendar
from typing import Dict, List
from database.repositories.transaction_repo import TransactionRepository

class ReportController:
    def __init__(self):
        self.repo = TransactionRepository()

    def get_50_30_20_analysis(self, monthly_income: float) -> dict:
        # Kategoria mapowania wg specyfikacji
        NEEDS = {"Jedzenie", "Mieszkanie", "Transport", "Zdrowie"}
        SAVINGS = {"Oszczędności"}
        wants_sum = 0.0
        needs_sum = 0.0
        savings_sum = 0.0

        now = date.today()
        transactions = self.repo.get_all({"year": now.year, "month": now.month})

        for t in transactions:
            if t.type != "expense":
                continue
            if t.category_name in NEEDS:
                needs_sum += t.amount
            elif t.category_name in SAVINGS:
                savings_sum += t.amount
            else:
                wants_sum += t.amount

        plan_needs = monthly_income * 0.5
        plan_wants = monthly_income * 0.3
        plan_savings = monthly_income * 0.2

        return {
            "needs": {
                "plan": plan_needs,
                "actual": needs_sum,
                "percent": (needs_sum / plan_needs * 100) if plan_needs else 0
            },
            "wants": {
                "plan": plan_wants,
                "actual": wants_sum,
                "percent": (wants_sum / plan_wants * 100) if plan_wants else 0
            },
            "savings": {
                "plan": plan_savings,
                "actual": savings_sum,
                "percent": (savings_sum / plan_savings * 100) if plan_savings else 0
            }
        }

    def forecast_spending(self, year: int, month: int) -> dict:
        transactions = self.repo.get_all({"year": year, "month": month})
        today = date.today()
        curr_day = today.day if today.month == month and today.year == year else 1
        days_in_month = calendar.monthrange(year, month)[1]

        spent_so_far = sum(t.amount for t in transactions if t.type == "expense" and t.date <= today)
        daily_avg = spent_so_far / curr_day if curr_day else 0
        forecast = daily_avg * days_in_month
        if month == 1:
            prev_year, prev_month = year - 1, 12
        else:
            prev_year, prev_month = year, month - 1
        prev_expenses = self.repo.get_all({"year": prev_year, "month": prev_month})
        budget_limit = sum(t.amount for t in prev_expenses if t.type == "expense")
        percent = (spent_so_far / budget_limit * 100) if budget_limit else 0
        if percent < 60:
            status = "ok"
        elif percent < 85:
            status = "warning"
        else:
            status = "danger"
        return {
            "spent_so_far": spent_so_far,
            "daily_avg": daily_avg,
            "forecast": forecast,
            "budget_limit": budget_limit,
            "percent": percent,
            "status": status
        }

    def what_if_simulation(self, monthly_saving: float, target: float) -> dict:
        if monthly_saving <= 0:
            return {
                "months": 0, "years": 0, "months_remainder": 0, "timeline": []
            }
        months_total = int(target // monthly_saving)
        remainder = target - months_total * monthly_saving
        months_remainder = 1 if remainder > 0 else 0
        timeline = []
        acc = 0.0
        for i in range(months_total + months_remainder):
            acc += monthly_saving
            acc = min(acc, target)
            timeline.append({"month": i+1, "amount": acc})
        total_months = months_total + months_remainder
        years = total_months // 12
        m_remainder = total_months % 12
        return {
            "months": total_months,
            "years": years,
            "months_remainder": m_remainder,
            "timeline": timeline
        }

    def get_monthly_trend(self, months: int = 6) -> List[dict]:
        now = date.today()
        result = []
        for i in range(months-1, -1, -1):
            year = now.year
            month = now.month - i
            if month <= 0:
                year -= 1
                month += 12
            txs = self.repo.get_all({"year": year, "month": month})
            income = sum(t.amount for t in txs if t.type == "income")
            expense = sum(t.amount for t in txs if t.type == "expense")
            m_name = date(year, month, 1).strftime("%b %Y").capitalize()
            result.append({"month": m_name, "income": income, "expense": expense})
        return result
