#Reverse the order of words in a sentence without changing the words themselves.

s = input("Enter a sentence: ")
words = s.split()
words.reverse()

print("Reversed sentence =", " ".join(words))
