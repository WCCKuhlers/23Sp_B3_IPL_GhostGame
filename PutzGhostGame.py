# Putz Ghost Game
from random import *

def ghostGame(localScore):

    score = localScore
    ghost_door = randint(1,3)
    usersel = input("There are Three Doors Ahead. \nA Ghost is behind one of the doors. \nPick a door: ")
    if (usersel == str(ghost_door)):
        score += 1
        print("Good Job! Your score is now " + str(score))
        ghostGame(score)
    elif usersel == "end":
        print("Thanks for playing! Your Final Score was " + str(score))
        start();
    elif usersel != "1" and usersel != "2" and usersel != "3" and usersel != "end":
        print("Invalid Syntax. Enter 1, 2, or 3, or alternatively end to end the game.")
        ghostGame(score)
    else:
        print("Nice Try! You selected Door " + usersel + ", and the door was " + str(ghost_door) + ". Score is still " + str(score))
        ghostGame(score)

print("Putz Ghost Game.")
ghostGame(0)
