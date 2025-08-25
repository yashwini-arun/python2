class Car:
    showroom = "XYZ Motors"

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def details(self):
        print(f"{self.brand} costs Rs.{self.price:.2f}")

# --- Main Program ---
cars = []
n = int(input("Enter number of cars: "))

for i in range(n):
    brand = input("Enter car brand: ")
    price = float(input("Enter car price: "))
    c = Car(brand, price)
    cars.append(c)

print("\n--- Showroom Cars ---")
for c in cars:
    c.details()
