n = int(input("Enter the number of rows = "))
for row in range(n):
    for column in range(row) :
        print(" ",end="")
    for column in range(n-row) :
        print("*",end=" ")
    print()