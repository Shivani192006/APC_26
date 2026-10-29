#3.Reverse a String 
#Reverse the given string without using built-in reverse functions.

s = input("Enter a string: ")
rev = ""

for ch in s:
    rev = ch + rev

print("Reverse =", rev)
