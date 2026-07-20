n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("")
for i in range(n,-1,-1):
    for j in range(1,i):
        print(j,end=" ")
    print("")

n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        if j == 1:
            print(" "*(n-i+1)+str(j),end=" ")
        else:
            print(j,end=" ")
    print("")

print("\n")

n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        if j == 1:
            print(" "*(n-i+1)+str(j),end=" ")
        else:
            print(j,end=" ")
    print("")
for i in range(n,-1,-1):
    for j in range(1,i):
        if j == 1:
            print(" "*(n-i+2)+str(j),end=" ")
        else:
            print(j,end=" ")
    print("")

n = 9
#upper
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("  "*2*(n-i),end="")
    for j in range(i,0,-1):
        print(j,end=" ")
    print("")
#middle
for j in range(1,2):
    for i in range(1,n+1):
        print(i, end=" ")
    for i in range(n,0,-1):
        print(i, end=" ")
    print("")
#lower
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("  "*2*(n-i),end="")
    for j in range(i,0,-1):
        print(j,end=" ")
    print("")
