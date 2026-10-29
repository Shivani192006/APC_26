#Write a program to count and display the total number of lines present in a text file.

f = open("student.txt", "r")
count = 0

for line in f:
    count += 1

print("Total lines =", count)
f.close()
