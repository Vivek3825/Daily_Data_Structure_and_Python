class employees:
    def __init__(self):
        self.__salary = 10000

    @property   # This decorator transforms method into managed attribute.
    def salary(self):  #getter function
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:       # Validation in setter.
            print("Invalid salary")
        else:
            self.__salary = value

    @salary.deleter
    def salary(self):
        del self.__salary


e = employees()

# print(e.__salary) Error: We can't access private attibutes or methods
#print(e.salary()) # Error: Due to @propert get method work as a attribute
print(e.salary)
e.salary = 20000
print(e.salary)
del e.salary
#print(e.salary) # Error: Cause salary got deleted
print(type(employees.salary))

"""
Reading: e.salary
calls:
@property
def salary(self):
________________________

Writing: e.salary = 1000
calls:
@salary.setter
________________________

Deleting: del e.salary
calls:
@salary.deleter
"""
