from dataclasses import dataclass
from typing import Optional

@dataclass
class SavingGoal:
    id: Optional[int]
    name: str
    target_amount: float
    current_amount: float = 0.0
    deadline: Optional[str] = None
    color: str = "#10B981"
    created_at: Optional[str] = None
