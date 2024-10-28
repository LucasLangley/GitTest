def filter_tasks_by_priority(self, priority):
        filtered_tasks = [task for task in self.tasks if task.priority == priority]
        for task in filtered_tasks:
            print(f"{task.description} - Prazo: {task.due_date} - Prioridade: {task.priority}")