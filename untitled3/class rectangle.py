class rectangle:

    def area(self):
        length = int(input("enter length of rectangle:"))
        breadth = int(input("enter breadth of rectangle:"))
        a=2*length +2*breadth
        print("area of rectangle is:",a)
r1=rectangle()
r1.area()