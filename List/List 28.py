scores = [45, 67, 102, 34, 89, 120, 55, 40, 101, 76]

centuries = 0
half_centuries = 0

for score in scores:
    if score >= 100:
        centuries += 1
    elif score >= 50:
        half_centuries += 1

print("Highest:", max(scores))
print("Lowest:", min(scores))
print("Total runs:", sum(scores))
print("Average:", sum(scores) / 10)
print("Centuries:", centuries)
print("Half-centuries:", half_centuries)
