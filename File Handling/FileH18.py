#Store employee ID, name, department, and salary in a file. Write functions to:  
#Display all employees.  
#Find the highest-paid employee.  
#Calculate average salary.  
#Display employees earning above a given salary.

def display():
    f = open("employee.txt", "r")
    print(f.read())
    f.close()

def highest_paid():
    f = open("employee.txt", "r")
    employees = []

    for line in f:
        id, name, dept, salary = line.strip().split(",")
        employees.append([id, name, dept, float(salary)])

    f.close()
    print("Highest paid:", max(employees, key=lambda x: x[3]))

def average_salary():
    f = open("employee.txt", "r")
    total = count = 0

    for line in f:
        salary = float(line.strip().split(",")[3])
        total += salary
        count += 1

    f.close()
    if count:
        print("Average salary =", total / count)

def above_salary(amount):
    f = open("employee.txt", "r")

    for line in f:
        data = line.strip().split(",")
        if float(data[3]) > amount:
            print(data)

    f.close()

f = open("employee.txt", "w")
f.write("101,Amit,IT,40000\n")
f.write("102,Priya,HR,50000\n")
f.write("103,Rahul,Sales,35000\n")
f.close()

display()
highest_paid()
average_salary()
above_salary(float(input("Enter salary: ")))
