#Accept a word from the user and search for it in a text file. Display the number of 
#occurrences and the line numbers where it appears.

f = open("student.txt", "r")
word = input("Enter word to search: ").lower()
count = 0

for i, line in enumerate(f, start=1):
    words = line.lower().split()

    if word in words:
        print("Found on line", i)
        count += words.count(word)

print("Total occurrences =", count)
f.close()
