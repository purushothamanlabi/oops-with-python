"""
Next, we should learn the core concepts of OOP:
1. Classes
2. Objects
3. Encapsulation
4. Inheritance
5. Polymorphism
6. Abstraction
"""

from abc import ABC, abstractmethod


class Engine:    # Example class to create an object and pass it to another class
    def start(self):
        return "Engine started"


class AbstractionBase(ABC):    # AbstractionBase says: abstract_action() must exist in all inherited classes
    @abstractmethod
    def abstract_action(self):
        pass


class MainClass(AbstractionBase):
    def __init__(self, brand, color):    # Constructor
        self.brand = brand              # Instance variables
        self.color = color

    def custom_function(self):
        return self.brand + " this is a function"

    def polymorphism(self):    # This will return if the object was created from this class
        return "polymorphism from parent"

    def __hidden_method_for_abstraction(self):    # This is a hidden mechanism
        return "background process completed"

    def abstract_action(self):
        message_from_background = self.__hidden_method_for_abstraction()
        return f"This is abstraction data from MainClass: {message_from_background}"


class SubClass(MainClass, Engine):                          # Inheritance with multiple classes
    school = "this is a class variable"                     # Class variable

    def __init__(self, price, brand, color, engine_object):
        self.engine_object = engine_object                  # Using another class object as a parameter we can call the function
        self.price = price
        self._private_message = "private"                   # Encapsulation: public = accessible anywhere | _protected = should be used inside class/child class | __private = should be used only inside class
        super().__init__(brand, color)

    def main_function(self):
        return "this is the main function"

    @property
    def secret_message(self):           # Access this as: child_instance.secret_message
        return f"Encapsulated message: {self._private_message}"

    def delete_private_message(self, password):    # This remains a method because it takes a 'password' argument
        if password == "dddd":
            self._private_message = ""
        return "Message deleted. Current message: " + self._private_message

    def polymorphism(self):             # Polymorphism = same method name, different behavior
        return "polymorphism from child"

    def abstract_action(self):
        return "this is abstraction data from SubClass"

    @classmethod                        # Takes cls parameter to access class variables and other methods
    def class_method_function(cls, new_data="this is default data"):    # Default parameter example
        cls.school = new_data
        return f"Class variable 'school' changed to: {cls.school}"

    @staticmethod                       # Static method — does not need a self parameter
    def add(a, b):
        return a + b

    def __str__(self):
        return "this is the __str__ function"


engine_instance = Engine()
main_instance = MainClass("fog", "blue")
child_instance = SubClass(666, "fog", "black", engine_instance)


print(child_instance.custom_function())
print(child_instance.delete_private_message("dddd"))
print(child_instance.polymorphism())
print(main_instance.polymorphism())
print(child_instance.__str__())
print(SubClass.mro())    # MRO tells the method resolution order (search order for methods)
print(isinstance(child_instance, MainClass))
print(issubclass(SubClass, MainClass))