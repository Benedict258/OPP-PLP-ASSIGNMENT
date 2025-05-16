# === Assignment 1: Superhero Class Design ===

class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self._power = power   # Protected attribute (encapsulation)
        self.origin = origin

    def display_info(self):
        print(f"{self.name} is from {self.origin} and has the power of {self._power}.")

    def use_power(self):
        print(f"{self.name} uses their power: {self._power}!")

# Subclass inheriting from Superhero
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def use_power(self):
        print(f"{self.name} flies at {self.flight_speed} km/h using their {self._power} power!")

# Creating objects
hero1 = Superhero("ElectroMan", "Electric Shock", "Electro City")
hero2 = FlyingSuperhero("SkyQueen", "Wind Control", "Cloud Realm", 800)

# Method calls
hero1.display_info()
hero1.use_power()

print("------")

hero2.display_info()
hero2.use_power()
