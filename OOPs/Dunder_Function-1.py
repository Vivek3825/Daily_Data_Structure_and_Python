class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.img = imaginary

    def show(self):
        print(self.real , 'i', "+", self.img , 'j')
    
    #Dunder Function
    def __add__(self, ComplexNum):
        NewReal = self.real + ComplexNum.real
        NewImaginary = self.img + ComplexNum.img
        return Complex(NewReal, NewImaginary)
    """
    self → refers to num1
    ComplexNum → refers to num2
    """
    
    # def __sub__(self, ComplexNum):
    #     NewReal = self.real + ComplexNum.real
    #     NewImaginary = self.img + ComplexNum.img
    #     return Complex(NewReal, NewImaginary)
    
num1 = Complex(2, 3)

num2 = Complex(4,5)

num1.show()
num2.show()

num3 = num1 + num2      # num1.__add__(num2)
# num3 = num1 - num2

num3.show()

"""
A dunder function (“double underscore function”) is a special built-in method in Python that starts and ends with __
They define how objects behave with operators and built-in functions.
"""