list=[]
n=int(input("enter number of elements for list:"))
print("enter elements for list:")
for i in range(0,n):
    e=int(input())
    list.append(e)
print(list)
mul=1
for item in list:
    mul=mul*item
print(mul)