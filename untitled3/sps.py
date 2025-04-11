print("1-stone")
print("2-paper")
print("3-scissor")
print("enter your choice ")
u1=int(input())
print("enter player 2 choice")
u2=int(input())
if u1==2 and u2==1 or u1==1 and u2==3 or u1==3 and u1==2 :
  print("you are winner")
elif u1==1 and u2==2 or u2==1 and u1==3 or u1==2 and u2==3:
  print("player 2 is winner")
else:
  print("game drop")





