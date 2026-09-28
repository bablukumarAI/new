n  = int(input("Enter the no's of lines :"))

for i in range(n):
    for j in range(n):
        if j == 0 or j == n - 1:
            print("*",end = "")
        else:
            print(" ", end = "")
    print()