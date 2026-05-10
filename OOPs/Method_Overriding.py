#Method Overriding
"""
Definition:
When a child class creates a method with the same name as the parent class method.
The child version replaces (overrides) the parent version.
"""

class car:
    def engine(self):
        print("Engine must be powerfull")

class Buggati(car):
    def engine(self):
        print("Buggati has 1800CC engine")
        super().engine()
 
obj = Buggati()
obj.engine()