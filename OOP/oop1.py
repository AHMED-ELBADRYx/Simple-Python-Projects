# Object attribute change function

from enum import Enum
from datetime import datetime
import json

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Status(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class Task:
    def __init__(self, name, description, due_date, priority=Priority.MEDIUM, status=Status.PENDING):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority if isinstance(priority, Priority) else Priority[priority.upper()]
        self.status = status if isinstance(status, Status) else Status[status.upper()]
        self.created_at = datetime.now()
        self.last_modified = datetime.now()

    def update_status(self, new_status):
        """Safely update task status with validation"""
        try:
            self.status = new_status if isinstance(new_status, Status) else Status[new_status.upper()]
            self.last_modified = datetime.now()
            return True
        except KeyError:
            print(f"❌ Invalid status. Available options: {[s.value for s in Status]}")
            return False

    def update_priority(self, new_priority):
        """Safely update task priority with validation"""
        try:
            self.priority = new_priority if isinstance(new_priority, Priority) else Priority[new_priority.upper()]
            self.last_modified = datetime.now()
            return True
        except KeyError:
            print(f"❌ Invalid priority. Available options: {[p.value for p in Priority]}")
            return False

    def update_due_date(self, new_date):
        """Update due date with format validation"""
        try:
            datetime.strptime(new_date, "%Y-%m-%d")
            self.due_date = new_date
            self.last_modified = datetime.now()
            return True
        except ValueError:
            print("❌ Invalid date format. Please use YYYY-MM-DD")
            return False

    def display_task(self, verbose=False):
        """Display task details with optional verbose output"""
        print(f"\n📋 Task: {self.name}")
        print(f"📝 Description: {self.description}")
        print(f"📅 Due Date: {self.due_date}")
        print(f"🔖 Priority: {self.priority.name.title()} ({self.priority.value})")
        print(f"🔄 Status: {self.status.value}")
        if verbose:
            print(f"⏱ Created: {self.created_at.strftime('%Y-%m-%d %H:%M')}")
            print(f"✏ Last Modified: {self.last_modified.strftime('%Y-%m-%d %H:%M')}")

    def to_dict(self):
        """Convert task to dictionary for serialization"""
        return {
            'name': self.name,
            'description': self.description,
            'due_date': self.due_date,
            'priority': self.priority.name,
            'status': self.status.name,
            'created_at': self.created_at.isoformat(),
            'last_modified': self.last_modified.isoformat()
        }

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the manager"""
        self.tasks.append(task)
        print(f"✅ Added task: {task.name}")

    def complete_task(self, task_name):
        """Mark a task as completed"""
        for task in self.tasks:
            if task.name.lower() == task_name.lower():
                if task.update_status(Status.COMPLETED):
                    print(f"✅ Marked '{task.name}' as completed")
                return
        print(f"❌ Task '{task_name}' not found")

    def display_all_tasks(self, verbose=False):
        """Display all tasks with optional details"""
        print("\n📋 All Tasks:")
        print("="*40)
        for task in self.tasks:
            task.display_task(verbose)
        print("="*40)

    def save_to_file(self, filename="tasks.json"):
        """Save tasks to JSON file"""
        with open(filename, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=2)
        print(f"💾 Saved {len(self.tasks)} tasks to {filename}")

# Example Usage
if __name__ == "__main__":
    manager = TaskManager()

    # Create and add tasks
    task1 = Task(
        "Complete project",
        "Finish the Python project with all requirements",
        "2023-05-15",
        Priority.HIGH,
        Status.IN_PROGRESS
    )

    task2 = Task(
        "Grocery shopping",
        "Buy milk, eggs, and bread",
        "2023-05-10",
        "medium",  # Will be converted to Priority enum
        "pending"  # Will be converted to Status enum
    )

    manager.add_task(task1)
    manager.add_task(task2)

    # Display all tasks
    manager.display_all_tasks(verbose=True)

    # Update task status
    manager.complete_task("Grocery shopping")

    # Try invalid status update
    task1.update_status("invalid_status")

    # Update task priority
    task1.update_priority("low")

    # Update due date
    task1.update_due_date("2023-05-20")

    # Display updated tasks
    manager.display_all_tasks(verbose=True)

    # Save tasks to file
    manager.save_to_file()