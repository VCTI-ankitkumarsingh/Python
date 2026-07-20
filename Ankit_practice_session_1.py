## Operators Statement
print("**Operators Statement**\n")
# Arithmetic Operators
a = 7
b = 17

# Arithmetic Operators
print("Arithmetic Operators")
print("a + b = ", a + b) #Add
print("a - b = ", a - b) #Subtract
print("a * b = ", a * b) #Multiply
print("a / b = ", a / b) #Divide
print("a "+"%"+" b = ", a % b) #Remainder
print("a ** b = ", a ** b) #Power
print("a // b = ", a // b) #Quotient

# Relational Operators
print("\nRelational Operators")
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# Assignment Operators
print("\nAssignment Operators")
x = 5
x += 2
print("x += 2: ", x)
x *= 3
print("x *= 3: ", x)
x -= 4
print("x -= 4: ", x)

# Logical Operators
print("\nLogical Operators")
print(a > b and b > 0)
print(a < b or b > 0)
print(not (a == b))

# Membership Operators
print("\nMembership Operators")
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)
print(10 not in numbers)

# Identity Operators
print("\nIdentity Operators")
list1 = [1, 2]
list2 = list1
list3 = [1, 2]

print(list1 is list2)
print(list1 is list3)
print(list1 == list3)

# Bitwise Operators
print("\nBitwise Operators")
p = 5 # 0101
q = 3 # 0011

print("AND : ", p & q)
print("OR : ", p | q)
print("XOR : ", p ^ q)
print("NOT : ", ~p)
print("Left Shift : ", p << 1)
print("Right Shift : ", p >> 1)

## Control Statements
print("\n**Control Statements**\n")

# If Statement
print("If Statements")
a = 10
b = 20

print("Is a >=b : ")
if a >= b:
    print("Tue")
else:
    print("False")

# For Loop
print("\nFor Statements")
for i in range(1, 10):
    print(i)

# While Loop
print("\nWhile Statements")
count = 1
while count <= 10:
    print(count)
    count += 1

# Break Statement
print("\nBreak Statements")
for i in range(1, 10):
    if i == 4:
        break
    print(i)

# Continue Statement
print("\nContinue Statements")
for i in range(1, 10):
    if i == 4:
        continue
    print(i)

# Pass Statement
print("\nPass Statements")
for i in range(1, 10):
    if i == 4:
        pass
    print(i)

## Write a program in which the object is immutable
print("\nWrite a program in which the object is immutable")
x = 10
print("Before:", x)
print("Before id:", id(x))

x = x + 5
print("After:", x)
print("After id:", id(x))

my_list = [1, 2, 3]
print(my_list)
print(id(my_list))

my_list.append(4)
my_list[0] = 10

print(my_list)
print(id(my_list))