import random

def computersTurn():
    return(random.choice(["rock", "paper", "scissors"]))

def whoWon(userChoice):
    compChoice = computersTurn()
    if compChoice == userChoice:
        print(f"Tie! user had {userChoice} and computer had {compChoice}")
    elif compChoice == "rock" and userChoice == "scissors":
        print("Computer Wins with rock:(")
    elif compChoice == "scissors" and userChoice == "paper":
        print("Computer Wins with scissors:(")
    elif compChoice == "paper" and userChoice == "rock":
        print("Computer Wins with paper:(")
    else:
        print(f"Player wins with {userChoice}, eat it!")

print("Playing against computer")
user_input = input("rock, paper, or scissors?: ")
whoWon(user_input)
