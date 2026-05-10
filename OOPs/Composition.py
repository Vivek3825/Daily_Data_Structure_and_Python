# Composition
"""
Composition means: One class contains another class object.

This creates a:
HAS-A relationship

instead of inheritance’s:
IS-A relationship
"""

class engine:
    def __init__(self):
        pass

    def start(self):
        print('Engine started....')

class car:
    def __init__(self):
        self.eng = engine()

    def start(self):
        self.eng.start()

obj = car()
obj.start()