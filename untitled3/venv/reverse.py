n=int(input("enter number to find reverse:"))
i=1
sum=0
while n>0:
    r=n%10
    sum=(sum *10)+r
    n=n//10
print("reverse number =",sum)
