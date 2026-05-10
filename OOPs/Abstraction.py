"""
Abstraction means: Hiding internal implementation details and showing only essential functionality to the user.

The user only knows:
what to do
not how it works internally
"""

from abc import ABC, abstractmethod

class vehicle(ABC):
    #@abstractmethod
    def __init__(self):
        pass
    @abstractmethod  # One abstract method is necessary for abstract class
    def start(self):
        print('How vehicle will start?')

    def show(self):
        print('Vehicle safety check from abstract class')

# we can use functionality of abstracted classes as we require

class bike(vehicle):
    def __init__(self):
        self.tyre = 2

    def start1(self):
        # super().show()
        # super().start()
        # print('Bike start with self start button')
        pass
    
    def start(self):
        super().show()
        super().start()
        print('Bike start with self start button')

"""
If a child class inherits from an abstract class, then it must implement all abstract methods to become a normal (concrete) class
Otherwise object creation is not allowed.
"""
    
class car(vehicle):
    def __init__(self):
        self.tyre = 4

    def start1(self):
        super().show()
        super().start()
        print('Car start with key')
        
#obj = vehicle() # We cannot create the objects of abstracted classes

obj1 = bike()
obj1.start()
