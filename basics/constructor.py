# class P:
#     def __init__(self):
#         print("Parent class constructor")

# class C(P):
#     def m1(self):
#         print("M1 method")

# obj = C()

class P:
    def __init__(self):
        print("Parent class constructor")

class C:
    def __init__(self):
        print("Child class constructor")

obj = C()