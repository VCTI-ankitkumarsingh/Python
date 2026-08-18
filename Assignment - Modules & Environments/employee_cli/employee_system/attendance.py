attendance_records = {}


def mark_attendance(employee_id, present=True):
    attendance_records.setdefault(employee_id, []).append(bool(present))
    return attendance_records[employee_id][-1]


def get_attendance(employee_id):
    return attendance_records.get(employee_id, []).copy()


def calculate_attendance_percentage(employee_id):
    records = get_attendance(employee_id)
    if not records:
        return 0.0
    return sum(records) / len(records) * 100
