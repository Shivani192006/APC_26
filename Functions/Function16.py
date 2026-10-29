def second_largest(lst):
    unique = []
    for n in lst:
        if n not in unique:
            unique.append(n)

    unique.sort()
    if len(unique) < 2:
        return "No second-largest number"
    return unique[-2]

lst = list(map(int, input("Enter numbers: ").split()))
print("Second largest =", second_largest(lst))
