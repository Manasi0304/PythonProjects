"""
class student:
    def __init__(self):
        print("this is my practical of default constructor")

s=student()
"""
class student:
    def __init__(self,name):
        self.name=name
    def show(self):
        print("this is parameterized constructor student name is :",self.name)
s=student("manasi")
s.show()