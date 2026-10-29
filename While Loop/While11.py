#Write a PYTHON program to find the sum of digits of given number

n = int(input("Enter a number: "))
s = 0

while n > 0:
    d = n % 10
    s = s + d
    n = n // 10

print("Sum of digits =", s)
