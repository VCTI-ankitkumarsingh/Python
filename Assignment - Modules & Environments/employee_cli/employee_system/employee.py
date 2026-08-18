employees = [
    {
        "id": "E001",
        "name": "John",
        "department": "IT",
        "salary": 50000,
    },
    {
        "id": "E002",
        "name": "Alice",
        "department": "HR",
        "salary": 45000,
    },
    {
        "id": "E003",
        "name": "Bob",
        "department": "Finance",
        "salary": 55000,
    },
]


def add_employee(employee_id, name, department, salary):
    if any(employee["id"] == employee_id for employee in employees):
        raise ValueError(f"Employee {employee_id} already exists.")

    employee = {
        "id": employee_id,
        "name": name,
        "department": department,
        "salary": salary,
    }
    employees.append(employee)
    return employee


def get_employee(employee_id):
    return next(
        (employee for employee in employees if employee["id"] == employee_id),
        None,
    )


def get_all_employees():
    return employees.copy()
