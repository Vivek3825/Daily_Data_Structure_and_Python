"""
A "dunder" function (short for Double Underscore) is a special method in Python that begins and ends with two underscores, 
such as __init__ or __str__. Also known as magic methods, 
they are not typically called directly by you; instead, 
the Python interpreter triggers them automatically during specific 
"""

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    # def __gt__(self, old):
    #     if self.price > old.price :
    #         return True
    #     elif self.price < old.price :
    #         return False

    def __gt__(self, old):
        return self.price > old.price
    
    #__gt__ is a dunder (double underscore) method for the greater than (>) operator.
        
item1 = Order("Watch", 70000)

item2 = Order("SmartWatch", 7000)

if item1 > item2:
    print(f"{item1.item} is expensive tham {item2.item}")
else:
    print(f"{item1.item} is not expensive tham {item2.item}")
        