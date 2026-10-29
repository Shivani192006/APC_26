#Validate a password based on these conditions: 
#Minimum 8 characters 
#At least one uppercase letter 
#One lowercase letter 
#One digit 
#One special character

s = input("Enter password: ")

upper = lower = digit = special = False

for ch in s:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    else:
        special = True

if len(s) >= 8 and upper and lower and digit and special:
    print("Valid password")
else:
    print("Invalid password")
