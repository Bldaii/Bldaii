CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    color TEXT DEFAULT '#3B82F6',
    icon TEXT DEFAULT '💰',
    type TEXT CHECK(type IN ('expense', 'income', 'both')) DEFAULT 'both',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    type TEXT CHECK(type IN ('income', 'expense')) NOT NULL,
    category_id INTEGER REFERENCES categories(id) ON DELETE SET NULL,
    description TEXT,
    date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS saving_goals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    target_amount REAL NOT NULL,
    current_amount REAL DEFAULT 0,
    deadline DATE,
    color TEXT DEFAULT '#10B981',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS settings (
    key TEXT PRIMARY KEY,
    value TEXT
);

-- Domyślne kategorie
INSERT OR IGNORE INTO categories (name, color, icon, type) VALUES
    ('Jedzenie', '#EF4444', '🍔', 'expense'),
    ('Transport', '#F59E0B', '🚗', 'expense'),
    ('Mieszkanie', '#8B5CF6', '🏠', 'expense'),
    ('Rozrywka', '#EC4899', '🎮', 'expense'),
    ('Zdrowie', '#06B6D4', '💊', 'expense'),
    ('Ubrania', '#84CC16', '👗', 'expense'),
    ('Oszczędności', '#10B981', '🏦', 'expense'),
    ('Inne wydatki', '#6B7280', '📦', 'expense'),
    ('Wynagrodzenie', '#10B981', '💼', 'income'),
    ('Freelance', '#3B82F6', '💻', 'income'),
    ('Inne przychody', '#6B7280', '💰', 'income');
