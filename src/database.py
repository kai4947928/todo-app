import sqlite3

DB_NAME = "todo.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            done INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    
def get_all_todos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, text, done FROM todos")
    todos = cursor.fetchall()
    conn.close()
    return todos

def add_todo(text):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, text, done FROM todos")
    todos = cursor.fetchall()
    conn.close()
    return todos

def add_todo(text):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO todos (text, done) VALUES (?, ?)",
        (text, 0)
    )
    conn.commit()
    conn.close()
    
def delete_todo(todo_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    conn.commit()
    conn.close()
    
def toggle_todo(todo_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT done FROM todos WHERE id = ?", (todo_id,))
    current = cursor.fetchone()

    if current:
        new_status = 0 if current[0] == 1 else 1
        cursor.execute(
            "UPDATE todos SET done = ? WHERE id = ?",
            (new_status, todo_id)
        )
        conn.commit()

    conn.close()