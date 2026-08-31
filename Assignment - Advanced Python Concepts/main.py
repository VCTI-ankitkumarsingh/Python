from employee_processor import employees
from report import generate_employee_report


def main():
    department = input("Enter department: ").strip()
    min_salary = int(input("Enter minimum salary: "))

    generate_employee_report(employees, department, min_salary)


if __name__ == "__main__":
    main()
