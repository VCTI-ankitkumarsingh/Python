students = {}

n = int(input("Enter number of students: "))
i = 0

while i < n:
    name = input("Enter student name: ")

    if not name.isalpha():
        print("Invalid name. Please enter a valid name.")
        continue

    while True:
        marks = float(input("Enter percentage marks: "))

        if 0 <= marks <= 100:
            students[name] = marks
            break
        else:
            print("Invalid marks. Please enter a value between 0 and 100.")

    i += 1

print("\nStudent Details:")
for name, marks in students.items():
    print(f"Name: {name}, Percentage: {marks}%")