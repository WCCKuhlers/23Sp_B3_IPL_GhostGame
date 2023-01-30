from random import randint
print ("Smith Monkey Collection")
start_game = True #sentinel value
score = 0
while start_game:
    monkey_door = randint(1,3)
    print("three doors ahead ")
    print("A Monkey Is behind you run!!!!! ")
    print("pick a door, enter 1, 2, or 3")
    user_door = input("1, 2, or 3")
    user_door_num = int(user_door)
    
    if monkey_door == user_door_num: #condition
        print("You found the MONKEY!")#true
        start_game = False
    else: #false
        print("You didn't find the MONKEY yet")
        score = score + 1

        print("Game  over.  you scored", score)
    
    #start_game = False
    #print ("The monkey door is: ", monkey_door)
    #print ("The players door is: ", user_door_num)
    
