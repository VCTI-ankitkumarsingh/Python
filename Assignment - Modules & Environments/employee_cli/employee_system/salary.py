def calculate_salary(base_salary, deduction=0):
    if base_salary < 0 or deduction < 0:
        raise ValueError("Salary and deduction cannot be negative.")
    return base_salary - deduction


def calculate_bonus(salary, percentage=10):
    if salary < 0 or percentage < 0:
        raise ValueError("Salary and percentage cannot be negative.")
    return salary * percentage / 100
