import datetime

''' Contains task class'''

class Task:
    """
    Represents a task in a task list that contains the name and time the task needs to
    be completed by

    Attributes
    ----------
        task_name: str
            Name of the task
        date: datetime.datetime
            Date of the task

    """
    def __init__(self, task_name: str, year: int, month: int, day: int, hour: int, minute: int, AM_or_PM: str):
        self.task_name = task_name
        if AM_or_PM == 'PM':
            hour += 12
        self.date = datetime.datetime(year, month, day, hour, minute)

    def __str__(self) -> str:
        """Returns a string of the date"""
        return (f"{self.task_name} needs to be done by {self.date.strftime("%x")} at "
                f"{self.date.strftime("%I")}:{self.date.strftime("%M")} {self.date.strftime("%p")}")

    def __repr__(self) -> str:
        """Returns a string of the method call"""
        return f"Task({self.task_name}, {self.date})"

    def __eq__(self, other: "Task") -> bool:
        return self.date == other.date

    def __gt__(self, other: "Task") -> bool:
        """Returns true if self.date comes after other.date"""
        return self.date > other.date

    def __lt__(self, other: "Task") -> bool:
        """Returns true if self.date comes before other.date"""
        return self.date < other.date

    def __ge__(self, other: "Task") -> bool:
        """Returns true if self.date comes after other.date"""
        return self.date >= other.date

    def __le__(self, other: "Task") -> bool:
        """Returns true if self.date comes before other.date"""
        return self.date <= other.date
    def change_date(self, year: int, month: int, day: int, hour: int, minute: int, am_or_pm: str):
        """Changes the date of the task"""
        if am_or_pm == 'PM':
            hour += 12
        self.date = datetime.datetime(year, month, day, hour, minute)



