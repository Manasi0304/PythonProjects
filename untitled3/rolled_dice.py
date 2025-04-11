("Rolling Dice Game")
import random
gamestart=input("please roll the dice(dice rolling):")
for i in range(10):
    player1_value = random.randint(1, 6)
    player2_value = random.randint(1, 6)
    print("Player 1 rolled: ", player1_value)
    print("Player 2 rolled: ", player2_value)
    if player1_value == 6:
        print("player 1 rolled: ",player1_value)
        if player1_value == 6:
            print("player 1 wins")
            break
    elif player2_value == 6:
        print("player 2 rolled: ",player2_value)
        if player2_value == 6:
            print("player 2 wins")
    else:
        print("player 1 rolled: ",player1_value)
        print("player 2 rolled: ",player2_value)
        continue
print("Game Over")