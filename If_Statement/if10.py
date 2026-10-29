#A company insures its drivers in the following cases:- If the driver is married.- If the driver is unmarried, male and above 30 years        
         #of age.      - If the driver is unmarried, female and above 25 years of age.
         
        #In all the other cases, the driver is not insured.        Write a PYTHON program to determine whether the driver     
        #is insured or not

marital_status = input("Enter marital status (married/unmarried): ")
gender = input("Enter gender (male/female): ")
age = int(input("Enter age: "))

if marital_status.lower() == "married":
    print("Driver is Insured")
elif marital_status.lower() == "unmarried" and gender.lower() == "male" and age > 30:
    print("Driver is Insured")
elif marital_status.lower() == "unmarried" and gender.lower() == "female" and age > 25:
    print("Driver is Insured")
else:
    print("Driver is Not Insured")
