class GPSMixin:
    def track_location(self, lat, lon):
        print(f"{self.name} current location → {lat}, {lon}")

class LoggerMixin:
    def log_action(self, action):
        print(f"[LOG] {self.name}: {action}")

class Vehicle:
    def __init__(self, name):
        self.name = name

class ElectricCar(Vehicle, GPSMixin, LoggerMixin):
    def drive(self):
        self.log_action("Driving...")
        print(f"{self.name} is moving!")

tesla = ElectricCar("Tesla Model Y")
tesla.drive()
tesla.track_location(12.97, 77.59)
