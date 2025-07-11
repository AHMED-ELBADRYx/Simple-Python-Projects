# Object attribute change function

class Task:
    def __init__(self, name, description, due_date, priority, status):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def display_task(self):
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Due Date: {self.due_date}")
        print(f"Priority: {self.priority}")
        print(f"Status: {self.status}")
        print()

    def mark_as_completed(self):
        self.status = "completed"

# Create tasks
task1 = Task("Buy groceries", "Milk, bread, eggs", "2023-04-30", "high", "pending")
task2 = Task("Clean the house", "Sweep the floors, take out the trash", "2023-04-29", "medium", "pending")

print("✅ Before changing the status:\n")
task1.display_task()
task2.display_task()

print("🛠 Changing status...\n")
task1.mark_as_completed()
task2.mark_as_completed()

print("✅ After changing the status:\n")
task1.display_task()
task2.display_task()