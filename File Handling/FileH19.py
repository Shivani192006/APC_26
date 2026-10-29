#Store student attendance records in a file. Calculate the attendance percentage and display 
#students having attendance below 75%.

f = open("attendance.txt", "w")
f.write("Amit,60,80\n")
f.write("Priya,55,80\n")
f.write("Rahul,70,80\n")
f.close()

f = open("attendance.txt", "r")

for line in f:
    name, present, total = line.strip().split(",")
    percentage = int(present) / int(total) * 100

    print(name, "Attendance =", percentage, "%")

    if percentage < 75:
        print(name, "has attendance below 75%")

f.close()
