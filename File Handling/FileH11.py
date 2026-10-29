#Read a text file and find the longest word present in the file.

f = open("student.txt", "r")
words = f.read().split()
f.close()

if words:
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    print("Longest word =", longest)
else:
    print("File is empty")
