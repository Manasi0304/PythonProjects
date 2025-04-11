class employee:
    count=0
    def __init__(self,name,des,sal):
        self.name=name
        self.des=des
        self.sal=sal
        employee.count=employee.count+1
    def displaycount(self):
        print(self.count)
    def displayemp(self):
        print(self.name)
        print(self.des)
        print(self.sal)
e1=employee("harish","manager",20000)
e2=employee("pranav","team leader",5000)
e1.displayemp()
e2.displayemp()
e1.displaycount()