class Employees:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("Employee role is:", self.role)
        print("Employee department is:", self.dept)
        print("Employee salary is:", self.salary)

class Engineer(Employees):
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age
        super().__init__("Engineer", "IT", 75000)
    
# super() is a built-in Python function used to access methods or constructors of the parent class.
# super() allows a child class to use functionality from its parent class without directly using the parent class name.


Emp1 = Engineer("Vivek", 22)
print("Employee name is:", Emp1.Name)
print("Employee Age is:", Emp1.Age) 
Emp1.showDetails()

# Emp1 = Employees("Accounter", "Finance", 45000)
# print("Employee name is:", Emp1.Name)
# print("Employee Age is:", Emp1.Age) 
# Emp1.showDetails()


 
