def r():
    return print("hey")
r()

#______________________________________________________________________________________________________________

class employees:
    def __init__(self):
        self.__salary = 10000   
    #Python internally renames __salary to _employees__salary to prevent accidental access

    def show(self):
        print(self.__salary)

e = employees()
e.__salary = 20000 # It create separate __salary variable
print(e.__salary)
e.show()