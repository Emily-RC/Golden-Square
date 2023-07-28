class Diary:

    def __init__(self):
        self.tasks = []

    def add_task(self, task_description: str) -> None:
        self.tasks.append(task_description)
        print(f"Task '{task_description}' was added to your diary.")

    def view_tasks(self) -> None:
        if not self.tasks:
            print("No tasks found.")
        else: 
            print("Todo Tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def complete_tasks(self, task_index: int) -> None:
        if 1 <= task_index <= len(self.tasks):
            completed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{completed_task}' marked as complete and removed from the list.")
        else:
            print("Invalid task index.")