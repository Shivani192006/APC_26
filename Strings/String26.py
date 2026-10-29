#Encrypt and decrypt a message using the Caesar Cipher algorithm.

s = input("Enter message: ")
choice = input("E for encrypt, D for decrypt: ").upper()
shift = int(input("Enter shift: "))
result = ""

if choice == "D":
    shift = -shift

for ch in s:
    if ch.isupper():
        result += chr((ord(ch) - 65 + shift) % 26 + 65)
    elif ch.islower():
        result += chr((ord(ch) - 97 + shift) % 26 + 97)
    else:
        result += ch

print("Result =", result)
