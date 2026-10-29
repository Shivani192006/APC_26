#Write a program to read a text file line by line and display each line separately.

f = open("student.txt", "r")

for line in f:
    print(line, end="")

f.close()
