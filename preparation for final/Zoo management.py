class Animal:
    def __init__(self, name, age, habitat):
        self.name = name
        self.age = age
        self.habitat = habitat
        self.is_available = True 
    
    def availability(self, status):
        self.is_available = status
        print(f"{self.name} is now {'available for viewing' if status else 'in quarantine'}.")
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Habitat: {self.habitat}")
        print(f"Available for Viewing: {'Yes' if self.is_available else 'No'}")

class Mammal(Animal):
    def __init__(self, name, age, habitat, fur_length, diet_type):
        super().__init__(name, age, habitat)
        self.fur_length = fur_length
        self.diet_type = diet_type
    
    def display_info(self):
        super().display_info()
        print(f"Fur Length: {self.fur_length}")
        print(f"Diet Type: {self.diet_type}")

class Bird(Animal):
    def __init__(self, name, age, habitat, wingspan, flight_altitude):
        super().__init__(name, age, habitat)
        self.wingspan = wingspan
        self.flight_altitude = flight_altitude
    
    def display_info(self):
        super().display_info()
        print(f"Wingspan: {self.wingspan}")
        print(f"Flight Altitude: {self.flight_altitude}")

class Reptile(Animal):
    def __init__(self, name, age, habitat, scale_pattern, venomous):
        super().__init__(name, age, habitat)
        self.scale_pattern = scale_pattern
        self.venomous = venomous
    
    def display_info(self):
        super().display_info()
        print(f"Scale Pattern: {self.scale_pattern}")
        print(f"Venomous: {'Yes' if self.venomous else 'No'}")


cat = Mammal("Cat", 3, "Homey", "Long", "Carnivore")
crow = Bird("Crow", 4, "City", "18 inches", "210 meters")
crocodile = Reptile("Crocodile", 7, "Pond", "Scaly", False)

print("Cat")
cat.display_info()
print("Crow")
crow.display_info()
print("Crocodile")
crocodile.display_info()

print("\nChanging Availability Status:")
cat.set_availability(False)
crow.set_availability(True)
crocodile.set_availability(False)

print("\nNew Animal Information:")
cat.display_info()
print("Crow")
crow.display_info()
print("\Crocodile")
crocodile.display_info()