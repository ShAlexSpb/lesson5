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

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}  # Пустой словарь для хранения ассортимента

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price


# Тестирование класса Task
task_manager = Task()
task_manager.add_task("Купить молоко", "2025-03-12")
task_manager.add_task("Посетить врача", "2025-03-15")
task_manager.complete_task(0)

task_manager.get_pending_tasks()
task_manager.get_completed_tasks()



# Тестирование класса Store
store1 = Store("Магазин Лакомка", "ул. Ленина, 1")
store2 = Store("Фруктовый Рай", "ул. Пушкина, 2")
store3 = Store("Все для дома", "ул. Гагарина, 3")

# Добавление товаров в магазины
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)
store2.add_item("апельсины", 0.8)
store3.add_item("швабра", 5)

# Тестирование методов на одном из магазинов
store1.update_price("яблоки", 0.55)
print(store1.get_price("яблоки"))  # Выводит 0.55
store1.remove_item("бананы")
print(store1.get_price("бананы"))  # Выводит None