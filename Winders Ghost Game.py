from random import randint
print("Stupid Ghost Game")
start_game = True #sentinal value
score = 0

while start_game:
    ghost_door = randint(1,3)
    print("Three doors ahead")
    print("A ghost is behind one of the doors...")
    print("Pick a door...see if your lucky...enter 1, 2, or 3...")
    user_door = input("1, 2, or 3")
    user_door_num = int(user_door)
    print("The ghost door is ", ghost_door)
    print("The players door is ", user_door_num)
    if user_door_num is ghost_door:
        start_game = False
        print("MWAHAHAHAHAHAAAA YOU LOSE!")
    
