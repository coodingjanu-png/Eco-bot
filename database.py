import sqlite3

connection = sqlite3.connect("economy.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    balance INTEGER DEFAULT 1000,
    bank INTEGER DEFAULT 0
)
""")

connection.commit()


def create_user(user_id: int):
    cursor.execute(
        "INSERT OR IGNORE INTO users (user_id) VALUES (?)",
        (user_id,)
    )
    connection.commit()


def get_user(user_id: int):
    create_user(user_id)

    cursor.execute(
        "SELECT balance, bank FROM users WHERE user_id = ?",
        (user_id,)
    )

    return cursor.fetchone()


def add_balance(user_id: int, amount: int):
    create_user(user_id)

    cursor.execute(
        "UPDATE users SET balance = balance + ? WHERE user_id = ?",
        (amount, user_id)
    )

    connection.commit()


def remove_balance(user_id: int, amount: int):
    create_user(user_id)

    cursor.execute(
        "UPDATE users SET balance = balance - ? WHERE user_id = ?",
        (amount, user_id)
    )

    connection.commit()
