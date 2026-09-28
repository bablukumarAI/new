class University:
    def __init__(self):
        self.uni_name = "Rajasthan technical university"

    class College:
        def __init__(self):
            self.college_name = "Arya college of engineering and IT"

        class Department:
            def __init__(self):
                self.dept__name = "Computer science and engineering"

            def display(self, uni_name, coll_name):
                print("University Name :", uni_name)
                print("College Name :", coll_name)
                print("Depatment Name :", self.dept__name)  

U = University()
C = U.College()
D = C.Department()

D.display(U.uni_name, C.college_name)