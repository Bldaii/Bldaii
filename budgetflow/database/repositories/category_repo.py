from models.category import Category
from database.db_manager import DBManager
from typing import Optional

class CategoryRepository:
    def __init__(self):
        self.conn = DBManager.get_instance().get_connection()

    def get_all(self, filters: dict = None) -> list:
        query = "SELECT * FROM categories WHERE 1=1"
        params = []
        if filters and "type" in filters:
            query += " AND (type = ? OR type = 'both')"
            params.append(filters["type"])
        query += " ORDER BY name"
        rows = self.conn.execute(query, params).fetchall()
        return [Category(**dict(row)) for row in rows]

    def get_by_id(self, id: int) -> Optional[Category]:
        row = self.conn.execute("SELECT * FROM categories WHERE id = ?", (id,)).fetchone()
        return Category(**dict(row)) if row else None

    def create(self, cat: Category) -> int:
        q = "INSERT INTO categories (name, color, icon, type) VALUES (?, ?, ?, ?)"
        cur = self.conn.cursor()
        cur.execute(q, (cat.name, cat.color, cat.icon, cat.type))
        self.conn.commit()
        return cur.lastrowid

    def update(self, cat: Category) -> bool:
        q = "UPDATE categories SET name = ?, color = ?, icon = ?, type = ? WHERE id = ?"
        cur = self.conn.cursor()
        cur.execute(q, (cat.name, cat.color, cat.icon, cat.type, cat.id))
        self.conn.commit()
        return cur.rowcount > 0

    def delete(self, id: int) -> bool:
        cur = self.conn.cursor()
        cur.execute("DELETE FROM categories WHERE id = ?", (id,))
        self.conn.commit()
        return cur.rowcount > 0
