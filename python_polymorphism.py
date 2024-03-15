""" Different classes with the same method(Method overloading) """
class Car:
    """
    A class representing an Car.
    """
def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    """
        Initializes an Car object.
 
        Parameters:
            brand (str): The brand of the car.
            model (int): The model of the car.
    """

def move():
    """
    This function just print the move result
    """
    print("Drive the car!")

class Boat:
    """
    A class representing an Boat.
    """
def __init__(self, brand, model):
    self.brand = brand
    self.model = model

def move():
    """
    This function just print the move result
    """
    print("Sail the boat!")

class Plane:
    """
    A class representing an Boat.
    """
def __init__(self, brand, model):
    self.brand = brand
    self.model = model

def move():
    """
    This function just print the move result
    """
    print("Fly in the Plane!")

# Create a Car object
car1 = Car("Ford", "Mustang")
# Create a Boat object
boat1 = Boat("Ibiza", "Touring 20")
# Create a Plane object
plane1 = Plane("Boeing", "747")

for val in (car1, boat1, plane1):
    val.move()
    print("------------------------------------------------")


# Inheritance Class Polymorphism(method overridding)
class Vehicle:
    """
    A class representing an Vehicle.
    """
def __init__(self, brand, model):
    self.brand = brand
    self.model = model

    """
        Initializes an Vehicle object.
 
        Parameters:
            brand (str): The brand of the car.
            model (int): The model of the car.
    """

def move():
    """
    This function just print the move result
    """
    print("Move!")

class Car(Vehicle):
    """
    A class representing an Car.
    """
    pass

class Boat(Vehicle):
    """
    A class representing an Boat.
    """
    def move(self):
        """
        This function just print the move result
        """
        print("Sail!")

class Plane(Vehicle):
    """
    A class representing an Plane.
    """
    def move(self):
        """
        This function just print the move result
        """
        print("Fly!")

# Create a Car object
car1 = Car("Ford", "Mustang")
# Create a Boat object
boat1 = Boat("Ibiza", "Touring 20")
# Create a Plane object
plane1 = Plane("Boeing", "747")

for val in (car1, boat1, plane1):
    print(val.brand)
    print(val.model)
    val.move()
