marks = [60, 70, 80, 55, 90, 65, 75, 85, 50, 95,
         45, 72, 68, 88, 77, 82, 58, 91, 63, 74]

average = sum(marks) / 20

above = 0
below = 0

for m in marks:
    if m > average:
        above += 1
    elif m < average:
        below += 1

print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Average:", average)
print("Above average:", above)
print("Below average:", below)
