import json
from datetime import datetime

class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            "description": self.description,
            "due_date": self.due_date,
            "priority": self.priority,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        task = Task(data["description"], data["due_date"], data["priority"])
        task.completed = data["completed"]
        return task

# task_manager.py

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.tasks = []
        self.filename = filename

    def add_task(self, description, due_date, priority):
        task = Task(description, due_date, priority)
        self.tasks.append(task)
        print(f"Tarefa '{description}' adicionada com sucesso!")

    def list_tasks(self, completed=False):
        tasks = [task for task in self.tasks if task.completed == completed]
        for idx, task in enumerate(tasks, start=1):
            status = "Concluída" if task.completed else "Pendente"
            print(f"{idx}. {task.description} - Prazo: {task.due_date} - Prioridade: {task.priority} - Status: {status}")
