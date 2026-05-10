class account():
    #__init__ is a special method (constructor) in Python that runs automatically when an object is created.
    def __init__(self):    #self in Python is a reference to the current instance (object) of a class.
        pass

    """
    self → refers to the current object
    __init__ → initializes the object's data (Constructor)
    """

    def create_account(self, account_num):
        self.balance = 0.0
        self.account_num = account_num
        print("\n____________________________________________")
        print("\nYour account number is:", self.account_num)
        print("Your account balance is:", self.balance)
        print("\n____________________________________________\n")


    def check(self):
        return self.balance
    
    def credit(self, ammount):
        self.balance += ammount
        print(f"Trasaction successfull, Avl Bal: {self.balance} Rs.\n")
        print("\n____________________________________________________________\n")

    def debit(self, ammount):
        if ammount <= self.balance:
            self.balance -= ammount
            print(f"Trasaction successfull, Avl Bal: {self.balance} Rs.")
        else:
            print(f"\n!Insufficient balance, Avl Bal: {self.balance} Rs.")
        print("\n____________________________________________________________\n")


    
i = 1
while i == 1:
    print("" 
        "\nTo create account in bank please enter: 1\n"
        "To check your account balance please enter: 2\n"
        "To withdraw a money please enter: 3\n"
        "To add money in your account please enter: 4\n"
        "To exit please enter: 0\n"
    "")
    choice = int(input("Enter your choice here => "))
    if choice == 1:
        user = account()
        user.create_account(1001)
    elif choice == 2:
        print("\n____________________________________________\n")
        print(f"Available Balance is: {user.check()}")
        print("\n____________________________________________\n")
    elif choice == 3:
        print("\n____________________________________________________________\n")
        money = int(input("Enter withdraw ammount: "))
        user.debit(money)
    elif choice == 4:
        print("\n____________________________________________________________\n")
        money = int(input("Enter adding ammount: "))
        user.credit(money)
    elif choice == 0:
        i = 0
    else:
        print("\n_______Please enter valid choice_______")