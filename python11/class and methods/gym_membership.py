class Member:
    gym = "Gold’s Gym"

    def __init__(self, name, months, fee):
        self.name = name
        self.months = months
        self.fee = fee

    def total_fee(self):
        return self.months * self.fee

    def show(self):
        print(f"{self.name}: {self.months} months | Total Rs.{self.total_fee():.2f}")

# --- Main Program ---
members = []
n = int(input("Enter number of members: "))

for i in range(n):
    name = input("Enter member name: ")
    months = int(input("Enter number of months: "))
    fee = float(input("Enter monthly fee: "))
    m = Member(name, months, fee)
    members.append(m)

print("\n--- Gym Memberships ---")
for m in members:
    m.show()
