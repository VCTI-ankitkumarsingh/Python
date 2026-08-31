employees = [
    {"id": 101, "name": "John", "department": "IT", "salary": 50000},
    {"id": 102, "name": "Mary", "department": "HR", "salary": 45000},
    {"id": 103, "name": "David", "department": "IT", "salary": 65000},
    {"id": 104, "name": "Sarah", "department": "Finance", "salary": 55000},
    {"id": 105, "name": "Alex", "department": "IT", "salary": 75000},
    {"id": 106, "name": "Lisa", "department": "HR", "salary": 48000},
]


class EmployeeIterator:
    """Custom iterator that returns one employee at a time."""

    def __init__(self, employees):
        self.employees = employees
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.employees):
            raise StopIteration

        employee = self.employees[self.index]
        self.index += 1
        return employee


def employee_generator(employees):
    """Yield employees one at a time."""
    for employee in employees:
        yield employee


def filter_by_department(employees, department):
    """Yield only employees from the requested department."""
    for employee in employees:
        if employee["department"].lower() == department.lower():
            yield employee


def create_salary_filter(min_salary):
    """Return a closure that remembers min_salary."""

    def check(employee):
        return employee["salary"] >= min_salary

    return check
