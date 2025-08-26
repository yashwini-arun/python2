class RewardMixin:
    def add_rewards(self, points):
        self.rewards += points
        print(f"{points} points added. Total: {self.rewards}")

class CancelMixin:
    def cancel_booking(self):
        print(f"Booking {self.room} cancelled.")

class Booking:
    def __init__(self, customer, room):
        self.customer = customer
        self.room = room
        self.rewards = 0

class HotelBooking(Booking, RewardMixin, CancelMixin):
    pass

b = HotelBooking("Sneha", "Deluxe Room")
b.add_rewards(50)
b.cancel_booking()
