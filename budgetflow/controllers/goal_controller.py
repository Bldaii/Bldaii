from typing import Optional, List
from models.goal import SavingGoal
from database.repositories.goal_repo import GoalRepository

class GoalController:
    def __init__(self):
        self.repo = GoalRepository()

    def get_all(self) -> List[SavingGoal]:
        return self.repo.get_all()

    def get_by_id(self, id_: int) -> Optional[SavingGoal]:
        return self.repo.get_by_id(id_)

    def create(self, name: str, target_amount: float, current_amount: float = 0,
               deadline: str = None, color: str = "#10B981") -> SavingGoal:
        goal = SavingGoal(
            id=None,
            name=name,
            target_amount=target_amount,
            current_amount=current_amount,
            deadline=deadline,
            color=color,
        )
        new_id = self.repo.create(goal)
        return self.repo.get_by_id(new_id)

    def update(self, goal: SavingGoal) -> bool:
        return self.repo.update(goal)

    def delete(self, id_: int) -> bool:
        return self.repo.delete(id_)
