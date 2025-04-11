def simple_interest(p,t,r):
    print("principal amount is:",p)
    print("time period:",t)
    print("rate:",r)
    SI=(p*t*r)/100
    print("simple interest is:",SI)
    return SI
pr=int(input("enter principal"))
ti=int(input("enter time"))
ra=int(input("enter rate"))
simple_interest(pr,ti,ra)
