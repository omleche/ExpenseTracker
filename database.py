import sqlite3

def init_db():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT,
            amount REAL,
            category TEXT,
            date TEXT,
            vat_type TEXT,
            is_business INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def add_expense(description, amount, category, date, vat_type, is_business):
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO expenses (description, amount, category, date, vat_type, is_business)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (description, amount, category, date, vat_type, int(is_business)))
    conn.commit()
    conn.close()

def get_expenses():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('SELECT * FROM expenses')
    results = c.fetchall()
    conn.close()
    return results