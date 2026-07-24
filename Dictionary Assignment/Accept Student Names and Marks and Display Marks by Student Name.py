students = {}

n = int(input("Enter number of students: "))
i = 0

while i < n:

    while True:
        name = input("Enter student name: ")
        if name.isalpha():
            break
        print("Invalid name. Please enter a valid name.")

    while True:
        marks = float(input("Enter marks: "))
        if 0 <= marks <= 100:
            break
        print("Invalid marks. Please enter a value between 0 and 100.")

    students[name] = marks
    i += 1

search = input("\nEnter student name to search: ")

if search in students:
    print(f"{search} scored {students[search]} marks")
else:
    print("Student not found")