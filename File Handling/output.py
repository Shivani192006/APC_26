
f = open("student.txt", "w")

name = input("Enter name: ")
roll = input("Enter roll number: ")
branch = input("Enter branch: ")
sem = input("Enter semester: ")

f.write("Name: " + name + "\n")
f.write("Roll Number: " + roll + "\n")
f.write("Branch: " + branch + "\n")
f.write("Semester: " + sem + "\n")

f.close()
print("Data written successfully")
