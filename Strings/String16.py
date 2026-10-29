#Display the frequency of every character in a string.

s = input("Enter a string: ")
checked = ""

for ch in s:
    if ch not in checked:
        count = 0

        for x in s:
            if x == ch:
                count += 1

        print(ch, "=", count)
        checked += ch
