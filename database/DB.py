import sqlite3

DB_PATH = "bot.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        tg_id INTEGER PRIMARY KEY,
        name TEXT,
        streak INTEGER DEFAULT 0,
        longest_streak INTEGER DEFAULT 0,
        last_report_date TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        book_id INTEGER,
        pages INTEGER,
        date TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        title TEXT,
        author TEXT,
        total_pages INTEGER,
        current_page INTEGER DEFAULT 0
    )
    ''')

    conn.commit()
    conn.close()


def add_user(tg_id, name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT OR IGNORE INTO users (tg_id, name) VALUES (?, ?)",
        (tg_id, name)
    )
    conn.commit()
    conn.close()


def get_user(tg_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE tg_id = ?", (tg_id,))
    user = cursor.fetchone()
    conn.close()
    return user

if __name__ == "__main__":
    init_db()
    print('Ok')