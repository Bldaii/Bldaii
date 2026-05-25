from dataclasses import dataclass, field
from datetime import date
from typing import Optional

@dataclass
class Transaction:
    id: Optional[int]
    amount: float
    type: str          # 'income' | 'expense'
    category_id: Optional[int]
    description: str
    date: date
    category_name: Optional[str] = field(default=None)
    category_color: Optional[str] = field(default=None)
    category_icon: Optional[str] = field(default=None)
