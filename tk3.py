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
