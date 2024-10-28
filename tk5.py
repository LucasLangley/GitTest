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
