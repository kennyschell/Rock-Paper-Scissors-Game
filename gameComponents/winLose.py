from gameComponents import gameVars

# define a win / lose function and refer to it (invoke it) in our game loop
def winorlose(status):
    if status == "won":
        pre_message = "Holy moly, you won! Good on ya mate! "
    else:
        pre_message = "Aw shucks, it's not looking good for you my friend! "

    print(pre_message + 'Ready for another round? Please say yes.. I am so dreadfully lonely..')

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
            print("You're really saying bye? Oh.. Okay.. Please come back soon.. It gets so dark and lonely in here..")
            exit()
        else:
            print("You've gotta type either yes or no, you silly goose.")
            choice = False