#Write a program to count the total number of characters in a text file, including spaces.

f = open("student.txt", "r")
data = f.read()

print("Total characters =", len(data))
f.close()
