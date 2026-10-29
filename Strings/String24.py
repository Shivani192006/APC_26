#Find the character with the highest frequency.

s = input("Enter a string: ")
maximum = 0
character = ""

for ch in s:
    count = s.count(ch)

    if count > maximum:
        maximum = count
        character = ch

if s:
    print("Most frequent character =", character)
    print("Frequency =", maximum)
