#2.Character Count 
#Count the number of vowels, consonants, digits, spaces, and special characters in a given string

s = input("Enter a string: ")
v = c = d = sp = special = 0

for ch in s:
    if ch.lower() in "aeiou":
        v += 1
    elif ch.isalpha():
        c += 1
    elif ch.isdigit():
        d += 1
    elif ch == " ":
        sp += 1
    else:
        special += 1

print("Vowels =", v)
print("Consonants =", c)
print("Digits =", d)
print("Spaces =", sp)
print("Special characters =", special)
