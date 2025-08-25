class BankAccount:
    bank_name = "HDFC Bank"

    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f" {self.owner} deposited {amount}. New Balance: {self.balance}")
        else:
            print(" Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print(" Withdrawal amount must be positive.")
        elif amount > self.balance:
            raise ValueError(f"Insufficient funds! {self.owner}'s balance is {self.balance}")
        else:
            self.balance -= amount
            print(f"{self.owner} withdrew {amount}. New Balance: {self.balance}")

    def display(self):
        print(f"Account Holder: {self.owner}, Balance: {self.balance}")


# --- Main Program ---
accounts = []
n = int(input("Enter number of accounts to create: "))

for i in range(n):
    name = input(f"\nEnter name for account {i+1}: ")
    bal = float(input("Enter initial balance: "))
    acc = BankAccount(name, bal)
    accounts.append(acc)

print("\n--- Transactions ---")
for acc in accounts:
    acc.display()
    dep = float(input(f"Enter deposit amount for {acc.owner}: "))
    acc.deposit(dep)

    try:
        wd = float(input(f"Enter withdrawal amount for {acc.owner}: "))
        acc.withdraw(wd)
    except ValueError as e:
        print(e)

print("\n--- Final Account Details ---")
for acc in accounts:
    acc.display()
