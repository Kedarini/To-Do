from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

TASKS_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)


tasks = load_tasks()


@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add():
    taskname = request.form["taskname"]
    due_date = request.form.get("due_date", "")
    tasks.append({"name": taskname, "due_date": due_date})
    save_tasks(tasks)
    return redirect(url_for("index"))


@app.route("/edit/<int:task_index>", methods=["POST"])
def edit(task_index):
    taskname = request.form["taskname"]
    due_date = request.form.get("due_date", "")
    if 0 <= task_index < len(tasks):
        tasks[task_index] = {"name": taskname, "due_date": due_date}
        save_tasks(tasks)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
