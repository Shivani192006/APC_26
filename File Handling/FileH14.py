#Read a text file and replace all occurrences of a specified word with another word. Save 
#the modified text in the same file or a new file.

f = open("student.txt", "r")
data = f.read()
f.close()

old = input("Enter word to replace: ")
new = input("Enter new word: ")

data = data.replace(old, new)

f = open("student.txt", "w")
f.write(data)
f.close()

print("Word replaced successfully")
