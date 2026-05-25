from models.transaction import Transaction
from database.db_manager import DBManager
from typing import Optional

class TransactionRepository:
    def __init__(self):
        self.conn = DBManager.get_instance().get_connection()

    def get_all(self, filters: dict = None) -> list:
        query = """
            SELECT t.*, c.name AS category_name, c.color AS category_color, c.icon AS category_icon
            FROM transactions t
            LEFT JOIN categories c ON t.category_id = c.id
            WHERE 1=1
        """
        params = []
        if filters:
            if filters.get("month"):
                query += " AND strftime('%m', t.date) = ?"
                params.append(f"{filters['month']:02d}")
            if filters.get("year"):
                query += " AND strftime('%Y', t.date) = ?"
                params.append(str(filters["year"]))
            if filters.get("category_id"):
                query += " AND t.category_id = ?"
                params.append(filters["category_id"])
            if filters.get("type"):
                query += " AND t.type = ?"
                params.append(filters["type"])
        query += " ORDER BY t.date DESC, t.id DESC"
        rows = self.conn.execute(query, params).fetchall()
        return [Transaction(**dict(row)) for row in rows]

    def get_by_id(self, id: int) -> Optional[Transaction]:
        query = """
            SELECT t.*, c.name AS category_name, c.color AS category_color, c.icon AS category_icon
            FROM transactions t
            LEFT JOIN categories c ON t.category_id = c.id
            WHERE t.id = ?
        """
        row = self.conn.execute(query, (id,)).fetchone()
        return Transaction(**dict(row)) if row else None

    def create(self, transaction: Transaction) -> int:
        q = """
            INSERT INTO transactions (amount, type, category_id, description, date)
            VALUES (?, ?, ?, ?, ?)
        """
        cur = self.conn.cursor()
        cur.execute(q, (transaction.amount, transaction.type, transaction.category_id, transaction.description, transaction.date))
        self.conn.commit()
        return cur.lastrowid

    def update(self, transaction: Transaction) -> bool:
        q = """
            UPDATE transactions
            SET amount = ?, type = ?, category_id = ?, description = ?, date = ?
            WHERE id = ?
        """
        cur = self.conn.cursor()
        cur.execute(q, (transaction.amount, transaction.type, transaction.category_id, transaction.description, transaction.date, transaction.id))
        self.conn.commit()
        return cur.rowcount > 0

    def delete(self, id: int) -> bool:
        cur = self.conn.cursor()
        cur.execute("DELETE FROM transactions WHERE id = ?", (id,))
        self.conn.commit()
        return cur.rowcount > 0
