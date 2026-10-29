names = ["Amit", "Rahul", "Sneha"]
ages = [20, 25, 30]

# Add patient
names.append("Priya")
ages.append(22)

# Delete patient
names.remove("Rahul")
ages.pop(1)

# Search patient
name = input("Enter patient name: ")

if name in names:
    print("Patient found")
else:
    print("Patient not found")

# Display patients
for i in range(len(names)):
    print(names[i], ages[i])

print("Total patients:", len(names))
