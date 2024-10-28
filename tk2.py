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
