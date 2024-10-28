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


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, description, due_date, priority):
        task = Task(description, due_date, priority)
        self.tasks.append(task)
        print(f"Tarefa '{description}' adicionada com sucesso!")

    def list_tasks(self, completed=False):
        tasks = [task for task in self.tasks if task.completed == completed]
        for idx, task in enumerate(tasks, start=1):
            status = "Concluída" if task.completed else "Pendente"
            print(f"{idx}. {task.description} - Prazo: {task.due_date} - Prioridade: {task.priority} - Status: {status}")

    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()
            print(f"Tarefa '{self.tasks[index].description}' marcada como concluída!")
        else:
            print("Índice de tarefa inválido.")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks.pop(index)
            print(f"Tarefa '{task.description}' removida com sucesso!")
        else:
            print("Índice de tarefa inválido.")

    def filter_tasks_by_priority(self, priority):
        filtered_tasks = [task for task in self.tasks if task.priority == priority]
        for task in filtered_tasks:
            print(f"{task.description} - Prazo: {task.due_date} - Prioridade: {task.priority}")

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)
        print("Tarefas salvas com sucesso!")

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                tasks_data = json.load(file)
                self.tasks = [Task.from_dict(data) for data in tasks_data]
        except FileNotFoundError:
            self.tasks = []
        except json.JSONDecodeError:
            print("Erro ao carregar o arquivo de tarefas. Iniciando com lista vazia.")
            self.tasks = []
