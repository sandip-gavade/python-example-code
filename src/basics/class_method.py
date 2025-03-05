class Vehicle:
    wheels = 4  # Class attribute

    @classmethod
    def set_wheels(cls, num):
        """Modifies the class attribute 'wheels'"""
        cls.wheels = num

    @classmethod
    def get_wheels(cls):
        """Returns the number of wheels"""
        return cls.wheels

# Calling class methods
print(Vehicle.get_wheels())  # Output: 4
Vehicle.set_wheels(6)
print(Vehicle.get_wheels())  # Output: 6

# Subclass
class Bike(Vehicle):
    wheels = 2

print(Bike.get_wheels())  # Output: 2
