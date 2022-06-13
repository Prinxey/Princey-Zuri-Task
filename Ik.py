#importing required libraries
import random
#parsing response into a list
answers = ["R","P","S"]
#creatkng a loop to allow the game run and account for errors.
while True:
    print('''Rock,Paper,Scissors game is about to begin\nEnter R for ROCK\nP for Paper\nS for Scissors''')
    secret = random.choice(answers)
    trial = input("Rock, Paper ,Scissors? ")
    if trial == 'quit':
        print('You have exited the game!!')
        break
    elif trial.upper() not in answers:
        print("==============\nPlease enter 'R' , 'P' or 'S'!!!\n==============")
        continue
    elif secret == "P" and trial.upper() == "S":
        print("Player(Scissors): CPU(Paper)\nScissors beats Paper")
        print("Player wins !!!!")
        break
    elif secret == "S" and trial.upper() == "P":
        print("Player(Paper): CPU(Scissors)\nScissors beats Paper")
        print("CPU wins !!!")
        break
    elif secret == "P" and trial.upper() == "R":
        print("Player(Paper): CPU(Rock)\nPaper beats Rock")
        print("CPU wins !!!")
        break
    elif secret == "R" and trial.upper() == "P":
        print("Player(Rock): CPU(Paper)\nPaper beats Rock")
        print("Player wins !!!")
        break
    elif secret == "R" and trial.upper() == "S":
        print("Player(Scissors): CPU(Rock)\nRock beats Scissors")
        print("CPU wins !!!")
        break
    elif secret == "S" and trial.upper() == "R":
        print("Player(Rock): CPU(Scissors)\nRock beats Scissors")
        print("Player wins !!!")
        break
    elif trial.upper() == secret:
        print("===============\nThis is a tie Try again!\n==============")
        continue
