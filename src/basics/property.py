class Person:
    def __init__(self, name, age):
        self._name = name  # Protected attribute
        self._age = age

    @property
    def age(self):
        """Getter method for age"""
        return self._age

    @age.setter
    def age(self, value):
        """Setter method to validate age"""
        if value < 0:
            raise ValueError("Age cannot be negative!")
        self._age = value

    @age.deleter
    def age(self):
        """Deleter method to delete age"""
        del self._age

# Usage
p = Person("Alice", 25)
print(p.age)  # Calls @property -> 25

p.age = 30  # Calls @age.setter
print(p.age)  # Output: 30

# p.age = -5  # Raises ValueError: Age cannot be negative!

del p.age  # Calls @age.deleter
# print(p.age)  # AttributeError: 'Person' object has no attribute '_age'


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        """Computes area dynamically"""
        return 3.1416 * self._radius ** 2

c = Circle(5)
print(c.area)  # Output: 78.54
# c.area = 100  # AttributeError: can't set attribute



class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

emp = Employee(5000)
print(emp.salary)  # 5000
emp.salary = 6000  # No explicit setter call
print(emp.salary)  # 6000
