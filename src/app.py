from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todos = []

@app.route("/", methods=["GET", "POST"])
def index():
    
    if request.method == "POST":
        new_todo = request.form.get("todo")
        
        if new_todo:
            todos.append(new_todo)
            
        return redirect("/")
    
    return render_template("index.html", todos=todos)

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    
    if 0 <= todo_id < len(todos):
        todos.pop(todo_id)
    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)