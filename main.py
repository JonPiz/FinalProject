import time
import superHelperTotal as SHT
import helperPlayer as HP
import helperDice as HD

def main():
    print("\nWelcome to Jonathan's dice roll turn decider!")
    time.sleep(2)
    print("We will simulate dice rolls and compare them to ascertain who shall go first!\n")
    time.sleep(2)

    numPlayers = HP.ChoosePlayerCount()

    players = {} # To hold players to ensure new names are unique

    for _ in range(1, numPlayers + 1):
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
        print(f"{rank}. [{player}] Total Roll: " + SHT.StyleTotal(playerRoll, numPlayers))

    time.sleep(1)
    print(f"\nIt looks like " + SHT.StyleFirstPlayer(sortedPlayers) + " will start this game!!")
    time.sleep(1.5)
    print("Thank you for using my app! -Jonathan Pizzano\n")

main()