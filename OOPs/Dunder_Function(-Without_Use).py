class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.img = imaginary

    def show(self):
        print(self.real , 'i', "+", self.img , 'j')

    def add(self, ComplexNum):
        NewReal = self.real + ComplexNum.real
        NewImaginary = self.img + ComplexNum.img
        return Complex(NewReal, NewImaginary)
    # self → num2
    # ComplexNum → num1
    
num1 = Complex(2, 3)

num2 = Complex(4,5)

num1.show()
num2.show()

num3 = num2.add(num1)

num3.show()