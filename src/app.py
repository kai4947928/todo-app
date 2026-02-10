from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    todos = [
        "買い物",
        "課題",
        "運動"
    ]
    return render_template("index.html", todos=todos)

if __name__ == "__main__":
    app.run(debug=True)