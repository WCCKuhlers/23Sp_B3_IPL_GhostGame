# Thompson Ghost Game

from random import randint
print("Scary Ghost")
start_game = True #sentinel value
score = 0

while start_game:
    ghost_door = randint(1,3)
    print("Three doors ahead")
    print("A ghost is behind one of the doors and you have to get the right door to catch the ghost to win ")
    print("Pick a door, enter 1, 2, or 3")
    user_door = input("1, 2, or 3")
    user_door_num = int(user_door)
    start_game = False
    print("The Scary Ghosts Door: ", ghost_door)
    print("The Players Door: ", user_door_num)
