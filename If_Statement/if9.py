# Write a PYTHON program to check a year for leap year.

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print("The year is a Leap Year")
else:
    print("The year is not a Leap Year")
