#Create a file containing student records in the format: 
#RollNo,Name,Marks 
#101,Amit,85 
#102,Priya,92 
#103,Rahul,78

f = open("students.txt", "w")
f.write("RollNo,Name,Marks\n")
f.write("101,Amit,85\n")
f.write("102,Priya,92\n")
f.write("103,Rahul,78\n")
f.close()

f = open("students.txt", "r")
lines = f.readlines()
f.close()

students = []

for line in lines[1:]:
    roll, name, marks = line.strip().split(",")
    students.append([roll, name, int(marks)])

print("All records:")
for s in students:
    print(s)

highest = max(students, key=lambda x: x[2])
print("Highest marks:", highest)

total = 0
for s in students:
    total += s[2]

print("Average marks =", total / len(students))

print("Students scoring above 80:")
for s in students:
    if s[2] > 80:
        print(s)
