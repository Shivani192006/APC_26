salaries = [25000, 35000, 45000, 55000, 60000, 28000]

average = sum(salaries) / len(salaries)

above_50 = 0
below_30 = 0

for salary in salaries:
    if salary > 50000:
        above_50 += 1
    if salary < 30000:
        below_30 += 1

print("Highest:", max(salaries))
print("Lowest:", min(salaries))
print("Average:", average)
print("Above 50000:", above_50)
print("Below 30000:", below_30)
