# Inheritance
"""
Inheritance means:
A child class gets properties and methods of a parent class.

This helps:
Reuse code
Reduce repetition
Organize programs properly
"""

class parent:
    def __init__(self):
        print('This is parent class')
        print('_____________________________')


class child(parent):
    def __init__(self):
        print('This is child class')
        super().__init__()

"""
A. Single Inheritance
Definition: One child class inherits from one parent class.
Parent -> Child
"""

class vehicles:
    def __init__(self):
        print('This is a vehicle class')
        print('_____________________________')

class car(vehicles):
    def __init__(self):
        print('This is a car class')
        super().__init__()
        #vehicles.__init__(self)  # This breaks MRO chain


class BMW(car):
    def __init__(self):
        print('This is a BMW class')
        super().__init__()

class bike(vehicles):
    def __init__(self):
        print('This is a bike class')
        super().__init__()
        #vehicles.__init__(self)  # This breaks MRO chain


class EV(car, bike):
    def __init__(self):
        print('This is a EV class')
        super().__init__()


"""
B. Multiple Inheritance
Definition: One child class inherits from multiple parent classes.
car, bike -> EV 

"""

"""
C. Multilevel Inheritance
Definition: A child becomes parent for another class.
vehicles -> car -> BMW
"""

"""
D. Hierarchical Inheritance
Definition: Multiple child classes inherit from one parent.
vehivles -> car, bike
"""

"""
Python follows:MRO (Method Resolution Order)
It checks classes from left to right.
Order: 1st car, 2nd bike
super() does NOT mean:
"call my parent"

It means:
"call the NEXT class in MRO"
This is VERY important in Python multiple inheritance.
"""

obj0 = child()
obj1 = bike()
obj2 = BMW()
obj3 = EV()

print(EV.mro())