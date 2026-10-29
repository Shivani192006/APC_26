def count_element(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

lst = list(map(int, input("Enter list numbers: ").split()))
element = int(input("Enter element to count: "))
print("Occurrences =", count_element(lst, element))
