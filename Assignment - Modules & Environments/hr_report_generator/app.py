from jinja2 import Environment, FileSystemLoader
from prettytable import PrettyTable

from employee_system.employee import get_all_employees


def generate_employee_report(employee, environment):
    template = environment.get_template("employee_report.txt")
    return template.render(employee=employee)


def create_employee_table(employees):
    table = PrettyTable()
    table.field_names = ["ID", "Name", "Department", "Salary"]

    for employee in employees:
        table.add_row(
            [
                employee["id"],
                employee["name"],
                employee["department"],
                employee["salary"],
            ]
        )

    return table


environment = Environment(loader=FileSystemLoader("templates"))

employees = get_all_employees()

print("=" * 40)
print(" HR EMPLOYEE REPORT")
print("=" * 40)
print()

for employee in employees:
    print(generate_employee_report(employee, environment),"\n")

print("Employee Table")
print("==============")
print(create_employee_table(employees))

