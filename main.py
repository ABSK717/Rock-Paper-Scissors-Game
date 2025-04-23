import random

def start_game():

   

    #choices
    choices = ["Rock","Paper","Scissors"]

    #A user can decide how number of round they want to play
    num_of_rounds = int(input("Enter Number of Rounds: "))

    #check where number of round is less than 1
    if num_of_rounds < 1:
        num_of_rounds = 1 #Set default round 1

    print("========= START ==========")
    #play multi rounds Game 
    for round in range (1,num_of_rounds+1): 

        print(f"Round: {round}")
        #computer choice
        computer = random.choice(choices)

        #get user input
        user = input("\nEnter your choice here: ")

        #transform into upper case
        computer =  computer.capitalize()
        user = user.capitalize()

        #check valid user input
        if user not in choices:
            print("invalid choice! Try again..\n")
            print("-"*25)

            continue

        print(f"\nYour choice: {user}")
        print(f"computer_coice: {computer}")

        result = make_decision(computer,user)

        print(f"\nResult: {result}")
        print("-"*25)

    print('========= END ==========')

#This fucnction decide who win the game
def make_decision(computer,user):
    #check who win or its just a draw
    if user == computer:
        return "its draw!"

    elif user == "Rock" and computer == "Scissors":
        return "You win!"

    elif user == "scissors" and computer == "Paper":
        return "You win!"

    elif user == "Paper" and computer == "Rock":
        return "You win!"

    else:
        return "Computer win!"

#start the game
start_game()