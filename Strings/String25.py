#Find the second most frequently occurring character.

s = input("Enter a string: ")
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

values = sorted(set(freq.values()), reverse=True)

if len(values) >= 2:
    second = values[1]

    for ch in freq:
        if freq[ch] == second:
            print("Second most frequent =", ch)
            print("Frequency =", second)
            break
else:
    print("Second most frequent character not found")
