import random
print("1-stone")
print("2-paper")
print("3-scissor")

count1=0
count2=0

print("how many times you want to play?")
time=int(input())
i=1
while i<=time:
    cc =random.randint(1,3)
    print("computer enter ",cc)
    print("enter player choice ")
    pc=int(input())
    if cc==pc:
        print("tie")
    elif  cc==2 and pc==1 or cc==2 and pc==3 or cc==1 and pc==3:
        print("computer enter= ",cc,"player enter=",pc,"so computer win")
        count1=count1+1
    elif cc==1 and pc==2or cc==2 and pc==3 or cc==3 and pc==1:
        print("computer enter=",cc,"player enter=",pc,"so player win")
        count2=count2+1
    i=i+1
print("computer win a match ",count1, "times")
print("player win a match ",count2,"times")
