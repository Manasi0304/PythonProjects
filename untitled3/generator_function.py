def city_names():
    print("aurangabad")
    yield 1
    print("nashik")
    yield 2
    print("pune")
    yield 3
    print("mumbai")
    yield 4
    print("nagar")
print("main area starts")
a=city_names()
c1=a.__next__()
print(a)
b=city_names()
c2=a.__next__()
print(b)
print("main area ends ")