#Read a text file and count how many times each word occurs. Display the result using a dictionary.

f = open("student.txt", "r")
words = f.read().lower().split()
f.close()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)
