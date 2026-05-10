# Polymorphism
"""
Definition
One method name behaves differently depending on object.
"Poly" = many
"Morphism" = forms

Meaning:
One thing, many forms
"""

class animal:
    def sound(self):
        print('Animal Sound')

class dog(animal):
    def sound(self):
        print('Bark')

class cat:
    def sound(self):
        print('Meow')

a = [animal(), dog(), cat()]

for i in a:
    i.sound()
