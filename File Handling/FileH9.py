#Read a text file and count the number of vowels and consonants present in the file.

f = open("student.txt", "r")
data = f.read().lower()
v = c = 0

for ch in data:
    if ch in "aeiou":
        v += 1
    elif ch.isalpha():
        c += 1

print("Vowels =", v)
print("Consonants =", c)
f.close()
