def palindrome(value):
    value = str(value).lower()
    return value == value[::-1]

value = input("Enter a string or number: ")
if palindrome(value):
    print("Palindrome")
else:
    print("Not a palindrome")
