# Walser Door Game

from random import randint

print("I have no clue what this is")
start_game = True #sentinel value
score = 0

while start_game:
    ghost_door = randint(1,3)
    print("Three doors ahead")
    print("A space laser shark is behind one of the doors")
    print("Pick a door, enter 1, 2, or 3")
    user_door = input("1, 2, or 3")
    user_door_num = int(user_door)
    print("The space laser shark door is: ", ghost_door)
    print("The players door is: ", user_door_num)
    if ghost_door == user_door_num:
        print("You were eaten and/or lasered.")
        start_game = False
    else:
        print("You avoided the space laser shark! Yay!")
        score = score + 1
        if score == 1:
            print("You have survived", score, "door so far.")
        else:
            print("You have survived", score, "doors so far.")
        
        




