import time
import helperDice as HD
from ansi import ansi

def main():

    def ChoosePlayerName():
        while True:
            name = input("\nWhat should this player be called?: ").capitalize()
            if name in players:
                print("\nThis name already exists!!! All names must be unique. Try again.\n")
            else:
                return name

    while True:
        numPlayers = input("How many players? (12 max): ")
        if numPlayers.isdigit():
            numPlayersFixed = int(numPlayers)
            if numPlayersFixed > 12:
                print("The max this program can reliably handle is 12. Please try again.")
            elif numPlayersFixed < 2:
                print("Cannot have less than two whole players!! Please retry.")
            else:
                break
        else:
            print("Not a valid integer. Please try again.")

    # Assign rolls to players
    players = {}
    for i in range(1, numPlayersFixed + 1):
        time.sleep(.5)
        name = ChoosePlayerName()
        sum = HD.RollPlayerDice(name, numPlayersFixed)
        players[name] = sum

    time.sleep(.75)
    
    # Determine turn order
    sortedPlayers = sorted(players.items(), key=lambda x: x[1], reverse=True)

    # Print results
    print("\nTurn order (based on dice rolls):")
    for rank, (player, playerRoll) in enumerate(sortedPlayers, start=1):
        print(f"{rank}. [{player}] Total Roll: " + ansi.BOLD + ansi.UNDERLINE + HD.GradeTotal(playerRoll, numPlayersFixed) + f"{playerRoll}" + ansi.END)
        
    print("")

main()