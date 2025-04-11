class student:
        r=int(input("enter the roll number of student:"))
        n=input("enter the name of student:")
        m1=int(input("enter the marks in subject 1:"))
        m2=int(input("enter the marks in subject 2:"))
        m3=int(input("enter the marks in subject 3:"))
        def display(self):
            print("name of student :",student.n)
            print("roll number of student :",student.r)
            print("marks in subject 1", student.m1)
            print("marks in subject 2", student.m2)
            print("marks in subject 3", student.m3)
s1=student()

s1.display()