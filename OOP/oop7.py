# Apply the attribute to a specific object

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

    def mark_as_done(self):
        self.status = "Done"

# Create tasks
task1 = Task("Buy groceries", "Milk, bread, eggs", "2023-03-31", "High", "Not completed")
task2 = Task("Clean the house", "Sweep the floors, take out the trash", "2023-04-01", "Medium", "Not completed")

# Change status for task1
task1.mark_as_done()

print("✅ Task 1 after marking as done:\n")
task1.display_task()

print("-" * 30)
print("✅ Task 2 remains unchanged:\n")
task2.display_task()