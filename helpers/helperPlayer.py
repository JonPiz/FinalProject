def ChoosePlayerName(currentPlayers):
    while True:
        name = input(f"\nWhat should Player {len(currentPlayers) + 1} be called?: ").capitalize()
        if name in currentPlayers:
            print("\nThis name already exists!!! All names must be unique. Try again.")
        else:
            return name

def ChoosePlayerCount():
    while True:
        numPlayers = input("How many players?: ")
        if numPlayers.isdigit():
            numPlayersFixed = int(numPlayers)
            if numPlayersFixed < 2:
                print("Cannot have less than two whole players!! Please retry.")
            else:
                return numPlayersFixed
        else:
            print("Not a valid integer. Please try again.")