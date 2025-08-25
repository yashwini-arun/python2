class Flight:
    airline = "IndiGo"

    def __init__(self, passenger, seat):
        self.passenger = passenger
        self.seat = seat

    def details(self):
        print(f"Passenger: {self.passenger}, Seat: {self.seat}")

    @classmethod
    def airline_info(cls):
        print(f"Flights by {cls.airline}")

f1 = Flight("Rahul", "12A")
f2 = Flight("Priya", "15B")

Flight.airline_info()
f1.details()
f2.details()
