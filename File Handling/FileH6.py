#Write a program to count the total number of words present in a text file.

f = open("student.txt", "r")
data = f.read()
words = data.split()

print("Total words =", len(words))
f.close()
