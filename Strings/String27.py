#Validate whether a given email address follows a valid format.

email = input("Enter email: ")

if "@" in email and "." in email and email.index("@") < email.rindex(".") and " " not in email:
    print("Valid email")
else:
    print("Invalid email")
