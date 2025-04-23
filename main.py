import random

#choices
choices = ["Rock","Paper","Scissors"]

#get user input
user = input("Enter your choice: ")

#computer choice
computer = random.choice(choices)
print(F"computer_coice: {computer}")

#This fucnction decide who win the game
def make_decision(computer,user):
    if user == "Rock" and computer == "Scissors":
        print("You win!")
    elif user == "Scissors" and computer == "Paper":
        print("You win!")
    elif user == "Paper" and computer == "Rock":
        print("You win!")
    else:
        print("Computer win!")

#Call the function
make_decision(computer,user)