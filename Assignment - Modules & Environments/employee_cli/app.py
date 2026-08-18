from rich.console import Console
from rich.table import Table
from tabulate import tabulate

from employee_system.employee import get_all_employees


def show_tabulate(employees, tablefmt="grid"):
    print("Employee List - Tabulate")
    print("------------------------")
    print(tabulate(employees, headers="keys", tablefmt=tablefmt))
    print()


def show_rich(employees):
    console = Console()
    table = Table(title="Employee Details")

    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Department")
    table.add_column("Salary", justify="right")

    for employee in employees:
        table.add_row(
            employee["id"],
            employee["name"],
            employee["department"],
            str(employee["salary"]),
        )

    console.print(table)



employees = get_all_employees()

print("=" * 40)
print(" EMPLOYEE CLI APPLICATION")
print("=" * 40)
print()

show_tabulate(employees, tablefmt="grid")

# The assignment asks for experimenting with at least two Tabulate formats.
print("Employee List - Tabulate (simple)")
print("---------------------------------")
print(tabulate(employees, headers="keys", tablefmt="simple"))
print()

print("Employee List - Rich")
print("--------------------")
show_rich(employees)
