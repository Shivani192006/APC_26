temperature = [30, 32, 29, 35, 31, 33, 28, 36, 34, 30,
               29, 31, 32, 35, 37, 33, 30, 28, 29, 34,
               36, 31, 32, 33, 35, 30, 29, 38, 34, 31]

average = sum(temperature) / 30

above = 0
below = 0

for t in temperature:
    if t > average:
        above += 1
    elif t < average:
        below += 1

print("Hottest:", max(temperature))
print("Coldest:", min(temperature))
print("Average:", average)
print("Days above average:", above)
print("Days below average:", below)
