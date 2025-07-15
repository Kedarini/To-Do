from flask import Flask, render_template, request, redirect, url_for
import json
import os
from datetime import datetime, timedelta

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
    return render_template(
        "index.html",
        tasks=tasks,
        today=datetime.now().date(),
        yesterday=(datetime.now() - timedelta(days=1)).date(),
        tomorrow=(datetime.now() + timedelta(days=1)).date(),
    )


@app.route("/add", methods=["POST"])
def add():
    global tasks
    taskname = request.form["taskname"]
    due_date = request.form.get("due_date", "")
    tasks.append({"name": taskname, "due_date": due_date})
    save_tasks(tasks)
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):
    global tasks
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)
    return redirect(url_for("index"))


@app.route("/edit/<int:task_index>", methods=["POST"])
def edit(task_index):
    global tasks
    taskname = request.form["taskname"]
    due_date = request.form.get("due_date", "")
    if 0 <= task_index < len(tasks):
        tasks[task_index] = {"name": taskname, "due_date": due_date}
        save_tasks(tasks)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
