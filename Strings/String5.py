#Count the number of uppercase and lowercase letters in a string.

s = input("Enter a string: ")
u = l = 0

for ch in s:
    if ch.isupper():
        u += 1
    elif ch.islower():
        l += 1

print("Uppercase =", u)
print("Lowercase =", l)
