from functools import wraps
from employee_processor import (
    employee_generator,
    filter_by_department,
    create_salary_filter,
)


def log_execution(func):
    """Decorator that logs when a function starts and finishes."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[START] {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[END] {func.__name__}")
        return result

    return wrapper


class ReportFile:
    """Context manager for writing the employee report."""

    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, "w", encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        return False


@log_execution
def calculate_average_salary(employees):
    """Calculate the average salary of the supplied employees."""
    employees = list(employees)

    if not employees:
        return 0

    return sum(employee["salary"] for employee in employees) / len(employees)


@log_execution
def generate_employee_report(employees, department, min_salary):
    """Generate and save an employee report using all required concepts."""

    salary_filter = create_salary_filter(min_salary)

    # 1. Generator processes employees lazily.
    generated_employees = employee_generator(employees)

    # 2. Generator filters by department.
    department_employees = filter_by_department(
        generated_employees, department
    )

    # 3. Closure filters by minimum salary.
    filtered_employees = (
        employee
        for employee in department_employees
        if salary_filter(employee)
    )

    # Materialize once because we need to write the report and calculate
    # the average salary.
    selected_employees = list(filtered_employees)

    print("Generating report...")

    with ReportFile("employee_report.txt") as report:
        report.write("Employee Report\n")
        report.write("===============\n")
        report.write(f"Department: {department}\n")
        report.write(f"Minimum Salary: {min_salary}\n")

        for employee in selected_employees:
            line = (
                f"{employee['id']} - {employee['name']} - "
                f"{employee['department']} - {employee['salary']}\n"
            )
            report.write(line)
            print(line.strip())

        average = calculate_average_salary(selected_employees)
        report.write(f"Average Salary: {average:.2f}\n")

    print("Report saved successfully.")
    return selected_employees
