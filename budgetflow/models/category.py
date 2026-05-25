from dataclasses import dataclass
from typing import Optional

@dataclass
class Category:
    id: Optional[int]
    name: str
    color: str = "#3B82F6"
    icon: str = "💰"
    type: str = "both"        # 'expense' | 'income' | 'both'
    created_at: Optional[str] = None
