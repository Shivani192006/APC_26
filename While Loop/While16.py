#Write a PYTHON program to print smallest of n numbers

n = int(input("How many numbers? "))
smallest = int(input("Enter a number: "))
i = 2

while i <= n:
    x = int(input("Enter a number: "))
    if x < smallest:
        smallest = x
    i = i + 1

print("Smallest =", smallest)
