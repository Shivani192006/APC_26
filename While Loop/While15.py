#Write a PYTHON program to print the largest of n numbers

n = int(input("How many numbers? "))
i = 1
largest = int(input("Enter a number: "))
i = 2

while i <= n:
    x = int(input("Enter a number: "))
    if x > largest:
        largest = x
    i = i + 1

print("Largest =", largest)
