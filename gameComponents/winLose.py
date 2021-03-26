from gameComponents import gameVars

# define a win / lose function and refer to it (invoke it) in our game loop
def winorlose(status):
    if status == "won":
        pre_message = "Congrats, you've won the game! "
    else:
        pre_message = "You lost the game, sorry friend! "

    print(pre_message + 'Ready for another round?')

    choice = False

    while choice == False:
        choice = input("yes / no? ")

        if choice == "yes" or choice == "Yes" or choice == "yup" or choice == "yeah":
            # reset the game loop and start over again
            gameVars.player_lives = gameVars.total_lives
            gameVars.computer_lives = gameVars.total_lives
            gameVars.player_choice = False
        elif choice == "no" or choice == "No" or choice == "nope" or choice == "nah":
            # exit message and bye
            print("You chose to say bye.. Come back soon!")
            exit()
        else:
            print("Please type yes or no.")
            choice = False