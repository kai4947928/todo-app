import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("todo.db")
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

init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    
    if request.method == "POST":
        new_todo = request.form.get("todo")
        
        if new_todo:
            cursor.execute(
                "INSERT INTO todos (text, done) VALUES (?, ?)",
                (new_todo, 0)
            )
            conn.commit()
        conn.close()
        return redirect("/")
    cursor.execute("SELECT id, text, done FROM todos")
    todos = cursor.fetchall()
    conn.close()
            
    return render_template("index.html", todos=todos)

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM todos WHERE id = ?", (todo_id))
    conn.commit()
    conn.close()
    
    return redirect("/")

@app.route("/toggle/<int:todo_id>")
def toggle(todo_id):
    
    conn = sqlite3.connect("todo.db")
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
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)