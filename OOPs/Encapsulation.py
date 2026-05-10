"""
Definition
Encapsulation means:
hiding internal data and controlling access to it.
"""

class car:
    def __init__(self):
        self.price = 9000000
        self.__EngineCode = 'HD231F'
        self.__password = 'pass'

    def agent(self):
        code = input("Enter password: ")
        if code == self.__password:
            print('Engine Code: ', self.__EngineCode)
        else:
            print("You cannot access private things")

class Buggati(car):
    def access(self):
        print(self.price)
        #print(self.__EngineCode) 
        super().agent()

        

obj = Buggati()
obj.access()


#Another Example
print('____________________________________\n')
print('Apna Bank\n')

class BankAccount:

    def __init__(self):

        self.name = "Rahul"          # public

        self._balance = 50000        # protected

        self.__pin = 1234            # private

    def show_pin(self):

        print("PIN:", self.__pin)


class BankEmployee(BankAccount):

    def access(self):

        print(self.name)

        print(self._balance)

        # print(self.__pin)   ERROR


obj = BankEmployee()

obj.access()

obj.show_pin()