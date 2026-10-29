#Write a PYTHON program to print sum of natural numbers up to n

n = int(input("Enter n: "))
i = 1
s = 0

while i <= n:
    s = s + i
    i = i + 1

print("Sum =", s)
