#Schilling Goated Ghost Game
from random import randint
print("Goated Ghost Game")
start_game = True #sentinel value
score = 0

while start_game:
    ghost_door = randint(1,3)
    print("Three doors ahead")
    print("The Ghost of Tony is behind one of these doors")
    print("Pick a door. Enter 1, 2, or 3")
    user_door = input("1, 2, or 3")
    user_door_num = int(user_door)
    if user_door_num == ghost_door:
        print("Tony's Ghost caught you! You lose!") #TRUE
        if score == 1:
            print("You evaded Tony's Ghost through", score, "door.")
            start_game = False
        else:
            print("You evaded Tony's Ghost through", score, "doors.")
            start_game = False
    else: #FALSE
        print("You evade Tony's Ghost...For now.")
        score = score + 1
        print("Score:",score)
        
            


    #start_game = False
    #print("Tony's ghost is behind this door: ", (ghost_door))
    #print("You chose door:", (user_door_num))
    
                      
