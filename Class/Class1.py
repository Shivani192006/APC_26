class BankAccount:
    account_counter = 1000

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        BankAccount.account_counter += 1
        self.account_number = BankAccount.account_counter

    def deposit(self, amount):
        self.balance += amount
        print(amount, "deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn successfully.")
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Current Balance:", self.balance)

    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print("Transfer successful.")
        else:
            print("Insufficient balance for transfer!")


# Creating two bank accounts
account1 = BankAccount("Rahul")
account2 = BankAccount("Priya")

# Performing deposit and withdrawal
account1.deposit(5000)
account1.withdraw(1000)

account2.deposit(3000)
account2.withdraw(500)

# Transferring money between accounts
account1.transfer(2000, account2)

# Displaying final balances
print("\nAccount Details:")
account1.display_balance()
print()
account2.display_balance()
