n = int(input("Enter the no's of lines :"))

mid = n // 2
for i in range(n):
    for j in range(n):
        if j == 0 or j == n -1 or i== mid:
            print("*", end  = "")
        else:
            print(" ", end = "")
    print()