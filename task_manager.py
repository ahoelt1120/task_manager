from task import Task
"""Contains task manager class"""

class TaskManager:
     """
    Represents a task list that contains a list of task objects

    Attributes
    ----------
        tasks: list[Task]
           List of tasks in the tasklist

    """
    def __init__(self):
        self.tasks = []
        to_do = 0

    def __repr__(self):
        "Returns a string representation of task manager"
        return f"TaskManager()"

    def add_task(self, new_task: Task):
        """Adds a task to the task list"""
        self.tasks.append(new_task)

    def remove_task(self, name: str):
        """Removes a completed task from the tasklist"""
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)

    def change_task_date(self, name: str, year: int, month: int, day: int, hour: int, minute: int, am_or_pm: str):
        """Changes the due date of an existing task"""
        for task in self.tasks:
            if task.name == name:
                task.change_date(year, month, day, hour, minute)


    def print_tasks(self):
        """Prints all tasks in the list"""
        print("Tasks:")
        for task in self.tasks:
            print(task)

    def task_sort_time(self):
        """Sort tasks by how close they need to be completed to by current date using quick sort"""
        # Sorting in place using quicksort algorithm
        if len(self.tasks) == 0 or len(self.tasks) == 1:
            return

        # partition
        low = 0
        high = len(self.tasks) - 1

        self.task_quicksort(low, high)

    def task_quicksort(self, low, high):
        """Recursively performs quick sort on the due dates of the
        tasks in self.tasks"""
        if low < high:
            # Partitioning the list
            pivot = self.tasks[high]
            index = (low-1)
            for j in range(low, high):
                if self.tasks[j] < pivot:
                    index += 1
                    # Swapping self.tasks[index] and self.tasks[j]
                    temp = self.tasks[index]
                    self.tasks[index] = self.tasks[j]
                    self.tasks[j] = temp
            # Swapping self.tasks[index + 1] and self.tasks[high]
            temp = self.tasks[index + 1]
            self.tasks[index+1] = self.tasks[high]
            self.tasks[high] = temp
            # Recursive call to check both sides of the list
            self.task_quicksort(low, index)
            self.task_quicksort(index + 2, high)



# Testing basic implemetation of task manager
if __name__ == "__main__":
    homework = TaskManager()
    scienceAssign = Task("Science Homework", 2024, 2, 19, 3, 30, "PM")
    compAssign = Task("Computer Homework", 2024, 2, 18, 3, 30, "PM")
    mathAssign = Task("Math Homework",2024, 2, 17, 3, 30, "PM")

    homework.add_task(scienceAssign)
    homework.add_task(compAssign)
    homework.add_task(mathAssign)

    homework.task_sort_time()
    homework.print_tasks()



