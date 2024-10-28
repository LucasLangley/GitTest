if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Estudar Python", "2024-11-01", "alta")
    manager.list_tasks()
    manager.save_tasks()