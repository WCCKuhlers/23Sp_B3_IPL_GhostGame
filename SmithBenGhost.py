from random import randint
print ("Bens Ghost Game")
start_game = true #sentinel value
score = 0
while start Game:
    ghost_door = randint (1,3)
    print ("three doors ahead")
    print ("A Ghost is behind one of the doors")
    print ("pikc a door. enter 1, 2 ,3")
    user _door = input ("1, 2 , or 3")
    user_door num = int(user_door)

    if ghost_door == user_door_num: #condition
        print ("you found the ghost!") #TRUE
        start_game = False
    start_game = False
    else: # FALSE
        print ("you didn't find the Ghost yet")
        score = score + 1
        print ("Game Over. it took you", score, "tried to find the ghost")
   
    
