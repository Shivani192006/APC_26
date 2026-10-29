#Write a PYTHON program to check the entered  number is palindrome or not

n = int(input("Enter a number: "))
temp = n
rev = 0

while n > 0:
    d = n % 10
    rev = rev * 10 + d
    n = n // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not palindrome")
