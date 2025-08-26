class DiscountMixin:
    def apply_discount(self, percent):
        self.price -= self.price * (percent / 100)
        print(f"Discount applied! New price: {self.price}")

class ExportMixin:
    def export_dict(self):
        return self.__dict__

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Electronics(Product, DiscountMixin, ExportMixin):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

item = Electronics("Laptop", 50000, "2 years")
item.apply_discount(10)
print("Exported:", item.export_dict())
