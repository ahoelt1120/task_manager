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

    def __len__(self):
        return len(self.tasks)

    def add_task(self, new_task: Task):
        """Adds a task to the task list"""
        self.tasks.append(new_task)

    def remove_task(self, name: str):
        """Removes a completed task from the tasklist"""
        for task in self.tasks:
            if task.task_name == name:
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

    def task_quicksort(self, low, high):
        """Sort tasks by how close they need to be completed to by current date using quick sort"""

        # Sorting in place using quicksort algorithm
        if len(self.tasks) == 0 or len(self.tasks) == 1:
            return

        if low < high:
            # Find pivot element such that
            # element smaller than pivot are on the left
            # element greater than pivot are on the right
            pi = self.partition(low, high)

            # Recursive call on the left of pivot
            self.task_quicksort(low, pi - 1)

            # Recursive call on the right of pivot
            self.task_quicksort(pi + 1, high)

    def partition(self, low, high):
        """Recursively performs quick sort on the due dates of the
        tasks in self.tasks"""
        pivot = self.tasks[high]

        # pointer for greater element
        i = low - 1

        # traverse through all elements
        # compare each element with pivot
        for j in range(low, high):
            if self.tasks[j] <= pivot:
                # If element smaller than pivot is found
                # swap it with the greater element pointed by i
                i = i + 1

                # Swapping element at i with element at j
                (self.tasks[i], self.tasks[j]) = (self.tasks[j], self.tasks[i])

        # Swap the pivot element with the greater element specified by i
        (self.tasks[i + 1], self.tasks[high]) = (self.tasks[high], self.tasks[i + 1])

        # Return the position from where partition is done
        return i + 1



# Testing basic implemetation of task manager
if __name__ == "__main__":
    homework = TaskManager()
    langAssign = Task("Language Homework", 2024, 2, 18, 5, 30, "PM")
    scienceAssign = Task("Science Homework", 2024, 2, 19, 3, 30, "PM")
    compAssign = Task("Computer Homework", 2024, 2, 18, 4, 30, "PM")
    mathAssign = Task("Math Homework",2024, 2, 17, 3, 30, "PM")


    homework.add_task(scienceAssign)
    homework.add_task(compAssign)
    homework.add_task(mathAssign)
    homework.add_task(langAssign)

    homework.print_tasks()
    # partition
    low = 0
    high = len(homework) - 1
    homework.task_quicksort(low, high)
    homework.print_tasks()



