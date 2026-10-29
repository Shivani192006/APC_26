#Write a program to read a text file and display its lines in reverse order.

f = open("student.txt", "r")
lines = f.readlines()
f.close()

for line in lines[::-1]:
    print(line, end="")
