def largest(numbers):
    big = numbers[0]
    for n in numbers:
        if n > big:
            big = n
    return big

numbers = list(map(int, input("Enter numbers: ").split()))
print("Largest =", largest(numbers))
