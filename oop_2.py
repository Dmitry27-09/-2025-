
import datetime
from collections import defaultdict
from typing import Optional, Union


class DeadlineError(Exception):
    """Исключение для просроченных заданий."""
    pass


class Person:
    """Базовый класс для студента и учителя."""
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name


class Homework:
    """Класс для представления домашнего задания."""
    def __init__(self, text: str, days: int) -> None:
        self.text = text
        self.deadline = datetime.timedelta(days=days)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        """Проверяет, не истек ли срок выполнения задания."""
        return datetime.datetime.now() - self.created < self.deadline


class HomeworkResult:
    """Класс для представления результата выполнения домашнего задания."""
    def __init__(self, homework: Homework, solution: str, author: 'Student') -> None:
        if not isinstance(homework, Homework):
            raise TypeError('You gave a not Homework object')
        self.homework = homework
        self.solution = solution
        self.author = author
        self.created = datetime.datetime.now()


class Student(Person):
    """Класс для представления студента."""
    def do_homework(self, homework: Homework) -> Optional[HomeworkResult]:
        """Выполняет домашнее задание и возвращает результат."""
        if not homework.is_active():
            raise DeadlineError('You are late')
        return HomeworkResult(homework, 'Some solution', self)


class Teacher(Person):
    """Класс для представления учителя."""
    homework_done = defaultdict(list)  # Общая структура для всех учителей

    @staticmethod
    def create_homework(text: str, days: int) -> Homework:
        """Создает новое домашнее задание."""
        return Homework(text, days)

    def check_homework(self, homework_result: HomeworkResult) -> bool:
        """Проверяет результат выполнения домашнего задания."""
        if len(homework_result.solution) > 5:
            self.homework_done[homework_result.homework].append(homework_result)
            return True
        return False

    def reset_results(self, homework: Optional[Homework] = None) -> None:
        """Сбрасывает результаты выполнения домашних заданий."""
        if homework is None:
            self.homework_done.clear()
        else:
            self.homework_done.pop(homework, None)


if __name__ == '__main__':
    teacher = Teacher('Daniil', 'Shadrin')
    student = Student('Roman', 'Petrov')

    expired_homework = teacher.create_homework('Learn functions', 0)
    oop_homework = teacher.create_homework('Create 2 simple classes', 5)

    try:
        student.do_homework(oop_homework)
    except DeadlineError as e:
        print(e)

    homework_result = student.do_homework(oop_homework)
    if homework_result:
        #print('vvvvvvv')
        print(f"Result: {homework_result.solution}")

    teacher.check_homework(homework_result)
    teacher.reset_results(oop_homework)