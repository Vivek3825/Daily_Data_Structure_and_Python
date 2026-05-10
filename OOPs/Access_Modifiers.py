"""
Access modifiers control where variables and methods can be accessed.
Python has 3 types:
Public
Protected
Private
"""

class Demo:

    def __init__(self):

        self.public = "Public"

        self._protected = "Protected"

        self.__private = "Private"

    def show(self):
        print(self.public)
        print(self._protected)
        print(self.__private)

obj = Demo()

print(obj.public)

print(obj._protected)

#print(obj.__private)   ERROR

obj.show()


# In Python, protected is only a convention, not true restriction.
# Python does not strongly enforce protection like Java/C++.