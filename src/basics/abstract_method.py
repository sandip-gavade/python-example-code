from abc import ABC, abstractmethod

# Abstract base class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        """Abstract method that must be implemented by subclasses"""
        pass

# Concrete subclass
class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

# Trying to instantiate the abstract class will raise an error
# animal = Animal()  # TypeError: Can't instantiate abstract class Animal with abstract methods make_sound

dog = Dog()
print(dog.make_sound())  # Output: Woof! Woof!
