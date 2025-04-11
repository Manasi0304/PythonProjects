try:
    n1=int(input("enter first number:"))
    n2=int(input("enter second number:"))
    r=n1/n2
    print(r)
except ZeroDivisionError as e:
    print(e)