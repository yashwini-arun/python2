class Course:
    platform = "Udemy"

    def __init__(self, title, instructor, price):
        self.title = title
        self.instructor = instructor
        self.price = price

    def show(self):
        print(f"Course: {self.title}, Instructor: {self.instructor}, Price: Rs.{self.price:.2f}")

    @staticmethod
    def discount(price):
        return price * 0.8

# --- Main Program ---
courses = []
n = int(input("Enter number of courses: "))

for i in range(n):
    title = input("Enter course title: ")
    inst = input("Enter instructor name: ")
    price = float(input("Enter course price: "))
    c = Course(title, inst, price)
    courses.append(c)

print("\n--- Course List ---")
for c in courses:
    c.show()
    print("Discounted Price:", Course.discount(c.price))
