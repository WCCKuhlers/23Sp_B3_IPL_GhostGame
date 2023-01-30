# Murtic Ghost Game

from random import randint
print("Scary Ghost Game")
start_game = True #sentinel value
score = 0

while start_game:
    ghost_door = randint(1,3)
    print("Three doors ahead")
    print("A ghost is behind one of the doors")
    print("Pick a door, enter 1, 2, or 3")
    user_door = input("1, 2, or 3")
    user_door_num = int(user_door)

    if ghost_door == user_door_num: #condition
        print("You found the ghost!") #TRUE
        start_game = False
    else: #FALSE
            print("You didn't find the ghost")
            score = score + 1
print("Game Over. It took you" ,score, "tries to find the ghost")
            
        



    #start_game = False
    #print("The ghost door is: ", ghost_door)
    #print("The players door is: ", user_door_num)

        
