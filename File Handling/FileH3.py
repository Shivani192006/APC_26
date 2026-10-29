#Write a program to append additional student information to an existing file without 
#deleting its previous contents.

f = open("student.txt", "a")

name = input("Enter student name: ")
roll = input("Enter roll number: ")

f.write("\nName: " + name)
f.write("\nRoll Number: " + roll)

f.close()
print("Data appended successfully")
