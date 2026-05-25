import sqlite3
from pathlib import Path

class DBManager:
    _instance = None
    _conn = None

    @classmethod
    def get_instance(cls) -> 'DBManager':
        if cls._instance is None:
            cls._instance = DBManager()
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        db_path = Path.home() / ".budgetflow" / "budget.db"
        db_path.parent.mkdir(exist_ok=True)
        self._conn = sqlite3.connect(str(db_path), check_same_thread=False)
        self._conn.row_factory = sqlite3.Row
        self._execute_schema()

    def get_connection(self) -> sqlite3.Connection:
        return self._conn

    def _execute_schema(self):
        import os
        schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")
        try:
            with open(schema_path, "r", encoding="utf-8") as f:
                sql_script = f.read()
            self._conn.executescript(sql_script)
            self._conn.commit()
        except Exception as e:
            print(f"[DBManager] Błąd przy inicjalizacji schematu DB: {e}")
