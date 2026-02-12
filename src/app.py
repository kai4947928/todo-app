from flask import Flask, render_template, request, redirect
import database

app = Flask(__name__)

database.init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    
    if request.method == "POST":
        new_todo = request.form.get("todo")
        
        if new_todo:
            database.add_todo(new_todo)
            
        return redirect("/")
    
    todos = database.get_all_todos()
    return render_template("index.html", todos=todos)

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    database.delete_todo(todo_id)
    return redirect("/")

@app.route("/toggle/<int:todo_id>")
def toggle(todo_id):
    database.toggle_todo(todo_id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)