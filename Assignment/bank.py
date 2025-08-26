# 🔹 Mixins
class InterestMixin:
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"💰 Interest added: ₹{interest:.2f}. New Balance: ₹{self.balance:.2f}")

class NotificationMixin:
    def notify(self, message):
        print(f"Notification for {self.account_holder}: {message}")


# 🔹 Base Class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f" Deposited ₹{amount}. Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f" Withdrew ₹{amount}. Balance: ₹{self.balance}")
        else:
            print(" Insufficient funds!")


# 🔹 Inheritance + Mixins Combined
class SavingsAccount(BankAccount, InterestMixin, NotificationMixin):
    def __init__(self, account_holder, balance=0, interest_rate=0.03):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate


# 🔹 Program Execution with User Input
name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))
rate = float(input("Enter interest rate (e.g., 0.05 for 5%): "))

acc = SavingsAccount(name, balance, rate)

while True:
    print("\n--- Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Add Interest")
    print("4. Show Balance")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        amt = float(input("Enter deposit amount: "))
        acc.deposit(amt)
    elif choice == "2":
        amt = float(input("Enter withdrawal amount: "))
        acc.withdraw(amt)
    elif choice == "3":
        acc.add_interest()
    elif choice == "4":
        print(f" Current Balance: ₹{acc.balance}")
    elif choice == "5":
        acc.notify("Thank you for banking with us!")
        break
    else:
        print("Invalid choice! Please try again.")
