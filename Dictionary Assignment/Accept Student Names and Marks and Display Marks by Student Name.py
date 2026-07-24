students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks

search = input("\nEnter student name to search: ")

if search in students:
    print(search, "scored", students[search], "marks")
else:
    print("Student not found")