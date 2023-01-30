# Williams Ghost Game
from random import randint
print(" Blayze's Ghost game")
gameStart = True
score = 0
attempts = 0
while gameStart:
    attempts += 1
    ghostDoor = randint(1,3)
    print(f"score is {score}\n")
    
    print("Three doors ahead")
    print("A ghost i behind one of the doors")
    print("Pick a door, enter 1, 2, or 3")
    userDoor = 0
    try:
        userDoor = int(input("1, 2, or 3: "))
    except ValueError:
        print("\nError: enter a number\n")
    print()
    print("Ghost Door: ",ghostDoor)
    print("userDoor: ",userDoor)
    print()
    
    if userDoor == ghostDoor:
        print("you won")
        score += 1
        
    
    elif userDoor < 1 or userDoor > 3:
        print("Number is not between 1 and 3\n")

    elif not userDoor == ghostDoor:
        print("You did not find the ghost")
        

    print()
    print("Do you want to continue write y or n: ")
    
    gameStart = True if input("") == "y" else False
    if gameStart == False:
        print(f"Score is {score}\n with {attempts} attempts")
    
    
        
    
