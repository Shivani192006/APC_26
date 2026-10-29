#Write a PYTHON program to print sum of even numbers up to n

n = int(input("Enter n: "))
i = 2
s = 0

while i <= n:
    s = s + i
    i = i + 2

print("Sum =", s)
