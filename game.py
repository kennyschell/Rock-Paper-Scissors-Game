from random import randint

# re-import our game variables
from gameComponents import gameVars, winLose

while gameVars.player_choice is False:
    print("-_-_-_-_-_-_-_-_-//*// RPS GAME //*//-_-_-_-_-_-_-_-_-")
    print("AI Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
    print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-_-_-")
    print("Let's play! Choose your weapon, or type 'bye' to exit..\n") #\n means "new line"
    gameVars.player_choice = input("Choose rock, paper, or scissors: \n")

    if gameVars.player_choice == "bye":
        print("Tired of playing? Just type 'bye'!")
        exit()

    gameVars.computer_choice = gameVars.choices[randint(0, 2)]

    print("player picked: " + gameVars.player_choice)
    print("AI chose: " + gameVars.computer_choice)

    if gameVars.computer_choice == gameVars.player_choice:
        print("draw!")
    elif gameVars.computer_choice == "rock":
        if gameVars.player_choice == "scissors":
            gameVars.player_lives -= 1
            print("Yikes, you lose! player lives:", gameVars.player_lives)
        else:
            print("Woohoo, you win!")
            gameVars.computer_lives -= 1
    elif gameVars.computer_choice == "paper":
        if gameVars.player_choice == "rock":
            gameVars.player_lives -= 1
            print("Oh no, you lose! player lives:", gameVars.player_lives)
        else:
            print("Yippie, you win!")
            gameVars.computer_lives -= 1
    elif gameVars.computer_choice == "scissors":
        if gameVars.player_choice == "paper":
            gameVars.player_lives -= 1
            print("Bummer, you lose! player lives:", gameVars.player_lives)
        else:
            print("Way to go, you win!")
            gameVars.computer_lives -= 1

    if gameVars.player_lives == 0:
        winLose.winorlose("lost")
    elif gameVars.computer_lives == 0:
        winLose.winorlose("won")
    else:
        gameVars.player_choice = False
