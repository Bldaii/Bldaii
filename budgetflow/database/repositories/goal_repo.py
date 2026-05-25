from models.goal import SavingGoal
from database.db_manager import DBManager
from typing import Optional

class GoalRepository:
    def __init__(self):
        self.conn = DBManager.get_instance().get_connection()

    def get_all(self, filters: dict = None) -> list:
        query = "SELECT * FROM saving_goals WHERE 1=1"
        params = []
        # Możliwe przyszłe filtry
        query += " ORDER BY created_at DESC"
        rows = self.conn.execute(query, params).fetchall()
        return [SavingGoal(**dict(row)) for row in rows]

    def get_by_id(self, id: int) -> Optional[SavingGoal]:
        row = self.conn.execute("SELECT * FROM saving_goals WHERE id = ?", (id,)).fetchone()
        return SavingGoal(**dict(row)) if row else None

    def create(self, goal: SavingGoal) -> int:
        q = "INSERT INTO saving_goals (name, target_amount, current_amount, deadline, color) VALUES (?, ?, ?, ?, ?)"
        cur = self.conn.cursor()
        cur.execute(q, (goal.name, goal.target_amount, goal.current_amount, goal.deadline, goal.color))
        self.conn.commit()
        return cur.lastrowid

    def update(self, goal: SavingGoal) -> bool:
        q = "UPDATE saving_goals SET name = ?, target_amount = ?, current_amount = ?, deadline = ?, color = ? WHERE id = ?"
        cur = self.conn.cursor()
        cur.execute(q, (goal.name, goal.target_amount, goal.current_amount, goal.deadline, goal.color, goal.id))
        self.conn.commit()
        return cur.rowcount > 0

    def delete(self, id: int) -> bool:
        cur = self.conn.cursor()
        cur.execute("DELETE FROM saving_goals WHERE id = ?", (id,))
        self.conn.commit()
        return cur.rowcount > 0
