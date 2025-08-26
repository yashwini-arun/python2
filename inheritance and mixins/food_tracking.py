class InvoiceMixin:
    def generate_invoice(self): return f"{self.item} - ₹{self.price}"

class TrackMixin:
    def track_order(self, status): print(f"Order '{self.item}': {status}")

class RewardMixin:
    def add_rewards(self, points): 
        self.rewards += points; print(f"Rewards: {self.rewards}")

class Order:
    def __init__(self, item, price):
        self.item, self.price, self.rewards = item, price, 0

class PizzaOrder(Order, InvoiceMixin, TrackMixin, RewardMixin):
    def __init__(self, item, price, toppings):
        super().__init__(item, price); self.toppings = toppings
    def details(self): print(f"Pizza: {self.item}, Toppings: {self.toppings}")

pizza = PizzaOrder("Veggie Pizza", 399, ["Cheese", "Olives"])
pizza.details(); print("Invoice:", pizza.generate_invoice())
pizza.track_order("Out for delivery"); pizza.add_rewards(50)
