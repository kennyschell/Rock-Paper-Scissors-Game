from gameComponents import gameVars
    

def shoot():
    if gameVars.computer_choice == gameVars.player_choice:
        print("draw!")
    elif gameVars.computer_choice == "rock":
        if gameVars.player_choice == "scissors":
            gameVars.player_lives -= 1
            print("Yikes, you lose! Your lives are now:", gameVars.player_lives)
        else:
            print("Woohoo, you win!")
            gameVars.computer_lives -= 1
    elif gameVars.computer_choice == "paper":
        if gameVars.player_choice == "rock":
            gameVars.player_lives -= 1
            print("Oh no, you lose! Your lives are now:", gameVars.player_lives)
        else:
            print("Yippie, you win!")
            gameVars.computer_lives -= 1
    elif gameVars.computer_choice == "scissors":
        if gameVars.player_choice == "paper":
            gameVars.player_lives -= 1
            print("You lose, that bites! Your lives are now:", gameVars.player_lives)
        else:
            print("Way to go, you win!")
            gameVars.computer_lives -= 1