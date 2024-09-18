class Vehicle:
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.__price = price
        self.__is_available = True

    def display(self):
        print("Make: ", self.make)
        print ("Model: ", self. model)

    def check_availability(self):
        return self.__is_available

    def rent(self):
        if self.__is_available:
            self.__is_available = False
            print(" ", self.model, " has been rented")
        else:
            print(" ", self.model, "is not available")

    def return_vehicle(self):
        self.__is_available = True
        print(" ", self.model, "has been returned.")

    def calculate_rental_cost(self, days):
        return self.__price * days


class Car(Vehicle):
    pass


class SUV(Vehicle):
    pass


class Truck(Vehicle):
    pass


class RentalReservation:
    def __init__(self, customer, vehicle, start_date, end_date):
        self.customer = customer
        self.vehicle = vehicle
        self.start_date = start_date
        self.end_date = end_date

    def display_reservation(self):
        print("Customer: ", self.customer.get_name())
        print("Vehicle: ", self.vehicle.model)
        print("Start Date: ", self.start_date)
        print("End Date: ", self.end_date)


class Customer:
    def __init__(self, name, contact_info):
        self.__name = name
        self.__contact_info = contact_info
        self.rental_history = []

    def get_name(self):
        return self.__name

    def add_rental(self, reservation):
        self.rental_history.append(reservation)

    def display_rental_history(self):
        for reservation in self.rental_history:
            reservation.display_reservation()

def display(vehicle):
    vehicle.display()


car = Car("Honda", "Civic", 8596)
suv = SUV("Toyota", "Land Cruiser", 13456)
truck = Truck("Toyota", "VIGO", 17890)

customer = Customer("Alisha", "0334567890")
reservation = RentalReservation(customer, car, "13-09-2024", "17-09=2024")
customer.add_rental(reservation)

customer.display_rental_history()

display(car)
display(suv)
