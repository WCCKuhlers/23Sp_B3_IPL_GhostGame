# kuhlers ghost game

from random import randint
print ("Pick a door! Avoid the ghost!")
start_game = True #sentinetal value on wether on not the games going to work
score = 0

while start_game:
    ghost_door = randint (1,3)
    print("Three doors ahead. . .")
    print("watch out, a ghost will be behind one of the doors")
    print("Pick a door, enter 1, 2 , or 3")
    user_door = input ("1, 2, or 3")
    user_door_num = int(user_door)
    #start_game = False
    print("The ghost door is: ", ghost_door)
    print("The player door is: ", user_door_num)

if user_door_num == ghost_door: #condition
    print("YOU DIED") #TRUE
    start_game = False
    print ("you survived", score, "different doors! better luck next time. . . if there is a next time")
else: 
    print ("uh oh! more doors! continue on until you die")
    score = score + 1

#when writing T and F its usually [if true (do this)] [else false (do this)]
