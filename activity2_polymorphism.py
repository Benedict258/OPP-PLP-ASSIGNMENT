# === Activity 2: Polymorphism Challenge ===

class Vehicle:
    def move(self):
        print("Vehicle is moving...")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")

# Polymorphic function
def travel(vehicle):
    vehicle.move()

# Creating vehicle objects
car = Car()
plane = Plane()
boat = Boat()

# Testing polymorphism
travel(car)
travel(plane)
travel(boat)
