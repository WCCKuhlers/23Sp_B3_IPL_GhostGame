#Khachikyan Ghost Game
from random import randint
print ("Mane's Ghost Game")
start_game = True #sentinel value
score = 0

while start_game:
    ghost_door = randint (1,3)
    print ("Three doors ahead!")
    print ("A ghost is behind one of the doors")
    print ("Pick a door, enter 1, 2 or 3")
    user_door = input("1, 2 or 3")
    user_door_num = int(user_door)          #this changes it to a number
if ghost_door = = user_door_num:  #Condition
    print ("You found the GHOST!")   #true statement
    start_game = False
else:  #False statement
    print ("You didn't find the ghost yet, try again!")
    score = score + 1

print ("Game over. It took you", score, "tries to find the ghost")



    
    #start_game = False
#print("The ghost door is: ", ghost_door)
#print("The player's door is:", user_door_num)




    
# === data type is the same
# == is when you compare to see if they are the exact same or not
# = is when you assign something

#if (Condition):
#   TRUE
#else:
#    FALSE
