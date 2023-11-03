#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# write 'hello world' to the console
print("hello world")

def play_again():
    player = input("Do you want to play again? (yes/no) ")
    if player == "yes":
        player = True
    elif player == "no":
        player = None
    else:
        player = None
    return player

# create a cycle to play again
points = 0
player=True
while player:
    # create a list of play options
    option = input("Choose rock, paper o scissors ")    
    if option != "rock" and option != "paper" and option != "scissors":
        print("Invalid option")
        player = True
    else:
        import random
        # create a list of play options
        options = ["rock", "paper", "scissors"]
        # assign a random play to the computer
        computer = random.choice(options)
        print("You choose: " + option)
        print("Computer choose: " + computer)
        # create conditions to win
        if (option == computer):
            print("Tie!")
        elif (option == "rock"):
            if (computer == "paper"):
                print("You lose!", computer, "covers", option)
            else:
                print("You win!", option, "smashes", computer)
                points += 1
        elif (option == "paper"):
            if (computer == "scissors"):
                print("You lose!", computer, "cut", option)
            else:
                print("You win!", option, "covers", computer)
                points += 1
        elif (option == "scissors"):
            if (computer == "rock"):
                print("You lose...", computer, "smashes", option)
            else:
                print("You win!", option, "cut", computer)
                points += 1
        print("Your Points: " + str(points))
        player= play_again()

