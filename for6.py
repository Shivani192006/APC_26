# Write a PYTHON program to compute the cosine series
#cos(x) = 1 – x2 / 2! + x4 / 4! – x6 / 6! + … xn / n!

x = float(input("Enter X(in radians): "))
n = int(input("Enter number of terms: "))

sum = 1
sign = -1

for i in range(2, 2 * n + 1, 2):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    sum = sum + sign * (x ** i) / fact
    sign *= -1

print("Cosine series =", sum)
