# class student():
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     def show(self):
#         sum = 0
#         for i in self.marks:
#             sum += i
#         print(f"Avg of three subject is: {sum/3}")


# stu1 = student("Vivek", [22, 20, 21])

# stu1.show()


#_____________Another method__________________#


class student():
    def __init__(self):
        self.name = str(input("Enter a student name: "))
        self.marks = []
        for i in range(1,4):
            self.marks.append(int(input(f"Enter the marks of subject{i}: ")))
    
    def show(self,):
        sum = 0
        for i in self.marks:
            sum += i
        print(f"Avg of three subject is: {sum/3}")


stu1 = student()

stu1.show()