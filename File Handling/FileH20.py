#Store deposits and withdrawals in a file. Read the file and calculate:  
#Total deposits  
#Total withdrawals  
#Final balance  
#Largest transaction

f = open("transactions.txt", "w")
f.write("Deposit,5000\n")
f.write("Withdrawal,1000\n")
f.write("Deposit,3000\n")
f.close()

f = open("transactions.txt", "r")
deposit = withdrawal = 0
largest = 0

for line in f:
    typ, amount = line.strip().split(",")
    amount = float(amount)

    if typ == "Deposit":
        deposit += amount
    elif typ == "Withdrawal":
        withdrawal += amount

    if amount > largest:
        largest = amount

f.close()

print("Total deposits =", deposit)
print("Total withdrawals =", withdrawal)
print("Final balance =", deposit - withdrawal)
print("Largest transaction =", largest)
