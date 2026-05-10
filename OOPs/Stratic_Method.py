class check():
    """
    A static method does not use the object (self) or class (cls).
    the method does not need object data
    the method does not need class data
    """

    A = 'A random class variable'

    @staticmethod
    def __init__():
        print("I am a contructor")
        print('I can access class using cls:', check.A, '\n')

    @classmethod
    def hello1(cls):
        print("Hello1")
        print('I can access class using cls:', cls.A, '\n')
    """
    Instance method → method that works with object data using self
    @classmethod → method that works with class data using cls
    """

    @staticmethod
    def hello2():
        print("Hello2")

    @staticmethod
    def hello3():
        print("Hello3")

c = check()

c.hello1()
c.hello2()
c.hello3()

"""
cls and self are naming conventions; Python passes the first argument automatically based on method type
"""