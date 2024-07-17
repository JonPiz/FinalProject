def ChoosePlayerName(currentPlayers):
    while True:
        name = input("\nWhat should this player be called?: ").capitalize()
        if name in currentPlayers:
            print("\nThis name already exists!!! All names must be unique. Try again.")
        else:
            return name

def ChoosePlayerCount():
    while True:
        numPlayers = input("How many players? (12 max): ")
        if numPlayers.isdigit():
            numPlayersFixed = int(numPlayers)
            if numPlayersFixed > 12:
                print("The max this program can reliably handle is 12. Please try again.")
            elif numPlayersFixed < 2:
                print("Cannot have less than two whole players!! Please retry.")
            else:
                return numPlayersFixed
        else:
            print("Not a valid integer. Please try again.")