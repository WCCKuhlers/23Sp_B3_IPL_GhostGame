#Mastin Pick-a-door

from random import randint
print("Pick A Door!")
#Sentinal V
start_game = 3
score = 0

while start_game > 0: #Condition  Constant TRUE
    rght_door = randint(1,3)
    print("Three doors ahead")
    print("only one leads to the exit.")
    print("Pick a door, enter 1,2,or 3")
    user_door = input("1,2,or 3")
    user_door_num = int(user_door)
    print("The right door is:",rght_door)
    print("Your door is",user_door_num)
    if rght_door == user_door_num: #Condition Once True
        print ("That was the right door!")
        score = score + 1
        start_game=3
    else: #False
        print ("Wrong door!")
        start_game = start_game - 1
    print ("-----------")
    print("Your score is:", score)
    print ("you have", start_game, "lives left")
    print ("-----------")
    
        
