#Write a program to open a text file and display its complete contents.

f = open("student.txt", "r")
print(f.read())
f.close()
