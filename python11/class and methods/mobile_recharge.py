class Recharge:
    provider = "Jio"

    def __init__(self, number, plan, cost):
        self.number = number
        self.plan = plan
        self.cost = cost

    def show(self):
        print(f"Mobile: {self.number}, Plan: {self.plan}, Cost: Rs.{self.cost:.2f}")

# --- Main Program ---
recharges = []
n = int(input("Enter number of recharges: "))

for i in range(n):
    number = input("Enter mobile number: ")
    plan = input("Enter plan name: ")
    cost = float(input("Enter cost: "))
    r = Recharge(number, plan, cost)
    recharges.append(r)

print("\n--- Recharges ---")
for r in recharges:
    r.show()
