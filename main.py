import time
import helperPlayer as HP
import helperDice as HD
from ansi import ansi

def main():

    numPlayers = HP.ChoosePlayerCount()

    # Assign rolls to players
    players = {}
    for i in range(1, numPlayers + 1):
        time.sleep(.5)
        name = HP.ChoosePlayerName(players)
        sum = HD.RollPlayerDice(name, numPlayers)
        players[name] = sum

    time.sleep(.75)
    
    # Determine turn order
    sortedPlayers = sorted(players.items(), key=lambda x: x[1], reverse=True)

    # Print results
    print("\nTurn order (based on dice rolls):")
    for rank, (player, playerRoll) in enumerate(sortedPlayers, start=1):
        print(f"{rank}. [{player}] Total Roll: " + ansi.BOLD + ansi.UNDERLINE + HD.GradeTotal(playerRoll, numPlayers) + f"{playerRoll}" + ansi.END)
        
    print("")

main()