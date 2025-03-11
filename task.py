class Task:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        self.tasks.append({"description": description, "due_date": due_date, "is_completed": False})

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["is_completed"] = True

    def get_pending_tasks(self):
        print("Текущие задачи:")
        for task in self.tasks:
            if not task["is_completed"]:
                description = task["description"]
                due_date = task["due_date"]
                print(f'{description} (срок: {due_date}, статус: Не выполнено)')

    def get_completed_tasks(self):
        print("Выполненные  задачи:")
        for task in self.tasks:
            if task["is_completed"]:
                description = task["description"]
                due_date = task["due_date"]
                print(f'{description} (срок: {due_date}, статус: Не выполнено)')




task_manager = Task()
task_manager.add_task("Купить молоко", "2025-03-12")
task_manager.add_task("Посетить врача", "2025-03-15")
task_manager.complete_task(0)

task_manager.get_pending_tasks()
task_manager.get_completed_tasks()
