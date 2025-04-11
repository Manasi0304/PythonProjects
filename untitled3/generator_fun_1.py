def operation(x,y):
    print("addition=")
    z = x+y
    yield z
    print("substraction =")
    z = x-y
    yield z
    print("multiplication=")
    yield z
    print("divison=")
    z=x/y
    yield z
a=operation(10,20)
ad = a.__next__()
print(ad)
sub=a.__next__()
print(sub)