#to enter 1-15 number into list
"""
ls=[]
i=1;
while i<=15:
    ls.append(i)
    i=i+1
print(ls)

"""
"""
ls=[]
i=1
while i<=15:
    if i%2==0:
        ls.append(i)
    print(i)
    i=i+1
print(ls)
"""
"""
ls=[]
i=1
print("enter name of 5 students ")
while i<=5:
    ls.append(input())
    i=i+1
print(ls)
"""
#to print output [[1,2,3],[4,5,6],[,8,9]]
"""
ls=[]
num=1
i=0
while i<=2:
    ls.append([])
    while True:
        ls[i].append(num)
        if num%3==0:
            num=num+1
            break
        num=num+1
    i=i+1
print(ls)
"""
# to print output [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20-------]upto 100
ls=[]
i=1
num=1
while i<=20:
    ls.append([])
    while True :
      ls[i].append(num)
      if num%5==0:
         num=num+1
         break
      num=num+1
i=i+1
print(ls)