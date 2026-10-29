#Print all duplicate characters in a string.

s = input("Enter a string: ")
seen = ""
duplicate = ""

for ch in s:
    if ch in seen and ch not in duplicate:
        duplicate += ch
    else:
        seen += ch

print("Duplicate characters =", duplicate)
