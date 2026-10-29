#Read a text file and calculate the number of alphabets, digits, spaces, and special characters.

f = open("student.txt", "r")
data = f.read()
a = d = s = sp = 0

for ch in data:
    if ch.isalpha():
        a += 1
    elif ch.isdigit():
        d += 1
    elif ch == " ":
        s += 1
    elif ch != "\n" and ch != "\t":
        sp += 1

print("Alphabets =", a)
print("Digits =", d)
print("Spaces =", s)
print("Special characters =", sp)
f.close()
