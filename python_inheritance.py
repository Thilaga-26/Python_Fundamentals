""" Create a base class """
class Person:
    """
    A class representing an Person.
    """
    def __init__(self, fname, lname, age):
        self.firstname = fname
        self.lastname = lname
        self.age = age

    def printname(self):
        """
        Parameters:
            fname (str): The fname of the Person.
            lname (str): The lname of the Person.
        """
        print(self.firstname, self.lastname)

    def printage(self):
        """
        Parameters:
            age (int): The age of the Person.
        """
        print(self.age)

# Use the Person class to create an object, and then execute the printname method:
person = Person("John", "Doe",25)
person.printname()

# Create a derived class
class Student(Person):
    """
    A class representing an Student.
    """
    def __init__(self, fname, lname,age, year):
        # Use the super() Function
        super().__init__(fname, lname,age)
        # Add Properties
        self.graduationyear = year

    def welcome(self):
        """
         Parameters:
            fname (str): The fname of the Person.
            lname (str): The lname of the Person.
            year (int): The year of the Student.
        """
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

stu = Student("Mike", "Olsen",25, 2019)
stu.printname()
print(stu.graduationyear)
stu.welcome()
