from datetime import date
from typing import Optional, List, Dict
from models.transaction import Transaction
from database.repositories.transaction_repo import TransactionRepository

class TransactionController:
    def __init__(self):
        self.repo = TransactionRepository()

    def add_transaction(self, amount: float, type: str, category_id: int,
                        description: str, date_: date) -> Transaction:
        transaction = Transaction(
            id=None,
            amount=amount,
            type=type,
            category_id=category_id,
            description=description,
            date=date_
        )
        new_id = self.repo.create(transaction)
        return self.repo.get_by_id(new_id)

    def get_all(self, month: int = None, year: int = None,
                category_id: int = None, type_: str = None) -> List[Transaction]:
        filters = {}
        if month:
            filters['month'] = month
        if year:
            filters['year'] = year
        if category_id:
            filters['category_id'] = category_id
        if type_:
            filters['type'] = type_
        return self.repo.get_all(filters)

    def update_transaction(self, transaction: Transaction) -> bool:
        return self.repo.update(transaction)

    def delete_transaction(self, id: int) -> bool:
        return self.repo.delete(id)

    def get_monthly_summary(self, year: int, month: int) -> dict:
        """
        Zwraca: {"income": float, "expense": float, "balance": float,
                 "by_category": list[dict]}
        """
        transactions = self.repo.get_all({"year": year, "month": month})
        income = sum(t.amount for t in transactions if t.type == "income")
        expense = sum(t.amount for t in transactions if t.type == "expense")
        balance = income - expense

        # Suma wg kategorii
        by_cat = {}
        for t in transactions:
            if t.category_name not in by_cat:
                by_cat[t.category_name] = {
                    "amount": 0.0,
                    "type": t.type,
                    "color": t.category_color,
                    "icon": t.category_icon
                }
            by_cat[t.category_name]["amount"] += t.amount

        by_category = []
        for name, val in by_cat.items():
            by_category.append({
                "name": name,
                "amount": val["amount"],
                "type": val["type"],
                "color": val["color"],
                "icon": val["icon"]
            })

        return {
            "income": income,
            "expense": expense,
            "balance": balance,
            "by_category": by_category
        }
