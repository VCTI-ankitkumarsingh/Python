students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter percentage marks: "))
    students[name] = marks

print("\nStudent Details:")
for name, marks in students.items():
    print(f"Name: {name}, Percentage: {marks}%")