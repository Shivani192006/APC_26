students = ["Amit", "Rahul", "Sneha"]

print("Total students:", len(students))

name = input("Search student: ")

if name in students:
    print("Student is present")
else:
    print("Student is absent")

students.append("Priya")
students.remove("Rahul")

print("Updated list:", students)
