#Count how many times a specific word appears in a sentence.

s = input("Enter a sentence: ").lower().split()
word = input("Enter a word: ").lower()
count = 0

for x in s:
    if x == word:
        count += 1

print("Occurrences =", count)
