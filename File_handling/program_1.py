file = open(r"C:\Users\bablu\OneDrive\Desktop\PYTHON\Name.txt","r")
#file.writelines("\nname : Ansh, class: CS-A, College: ARYA college of engineering and IT")
name = file.readlines()
#names.append(name)
file.close()

print(name)





    