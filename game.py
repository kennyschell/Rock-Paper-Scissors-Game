from random import randint
#re-import our game variables
from gameComponents import gameVars, winLose, comparisonCode
while gameVars.player_choice is False:
    print("-_-_-_-_-_-_-_-_-//*// RPS GAME //*//-_-_-_-_-_-_-_-_-")
    print("Frank's Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
    print("Your Lives:", gameVars.player_lives, "/", gameVars.total_lives)
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-_-_-")
    print("Welcome to Rock, Paper, Scissors with Frank! I'm Frank, and I live in your machine..Let's play! Go on, select a weapon! Or type 'bye' to leave me here all alone..\n") #\n means "new line"
    gameVars.player_choice = input("Select rock, paper, or scissors: \n")

    if gameVars.player_choice == "bye":
        print("Please don't leave me.. But if you must.. Go ahead and type 'bye'...")
        exit()

    gameVars.computer_choice = gameVars.choices[randint(0, 2)]

    print("I see you chose: " + gameVars.player_choice)
    print("I went with: " + gameVars.computer_choice)

    comparisonCode.shoot()

    if gameVars.player_lives == 0:
        winLose.winorlose("lost")

    if gameVars.computer_lives == 0:
        winLose.winorlose("won")

    gameVars.player_choice = False
