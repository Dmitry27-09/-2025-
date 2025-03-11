
import datetime


class Homework:
    def __init__(self, text: str, days: int) -> None:
        self.text = text
        self.deadline = datetime.timedelta(days=days)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        return datetime.datetime.now() - self.created < self.deadline


class Student:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def do_homework(self, homework: Homework) -> Homework | None:
        if not homework.is_active():
            print('You are late')
            return None
        return homework


class Teacher:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def create_homework(text: str, days: int) -> Homework:
        return Homework(text, days)


if __name__ == '__main__':
    teacher = Teacher('Daniil', 'Shadrin')
    student = Student('Roman', 'Petrov')

    expired_homework = teacher.create_homework('Learn functions', 0)
    oop_homework = teacher.create_homework('Create 2 simple classes', 5)

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  # You are late