import random
import time
first_six=False
player_num=1
while True:
    print("player",player_num,"play your turn...")
    print("press enter to rolled the dice....")

    input()

    score=random.randint(1,6)
    if score==6 and first_six==False :
        first_six==True
        print(player_num,"you rolled six....",score,"repeat your turn")
        continue
    elif score==6 and first_six==True:
        print(player_num,"rolled",score)
        print("you win!...")
        break
    else:
        first_six=False
        if player_num == 1:
            player_num =2
        elif player_num==2:
            player_num=1