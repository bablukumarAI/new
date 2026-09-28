file = open(r"C:\Users\bablu\OneDrive\Desktop\PYTHON\Name.txt")
name = file.readlines()
file.close()

file2 = open("sample.txt", "w")
file2.writelines(name)
file2.close()