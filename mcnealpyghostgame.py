# McNeal Ghost Game

from random import randint
print("McNeals Ghost Game")
start_game = True #sentinel value
score = 0

while start_game:
    ghost_door = randint(1,3)
    print("Three doors ahead")
    print("a ghost is behind one of the doors")
    print("please choose a door, enter 1, 2, or3")
    user_door = input("1, 2, or 3")
    user_door_num = int(user_door)
    #start_game = False
    print("The ghost was behind door: ", ghost_door)
    print("you chose door: ", user_door_num)
    
