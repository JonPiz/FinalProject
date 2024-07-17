import random
from ansi import ansi

def RollPlayerDice(playerName, totalPlayers):
    sum = 0
    for i in range(1, totalPlayers + 1):
        roll = random.randint(1, 6) # Simulated Dice Roll
        sum += roll
        color = GradeRoll(roll=roll)
        print(f"[{playerName}] Roll {i}: " + color + f"{roll} " + ansi.END , end="")
    print(f"\n[{playerName}] Sum: " + ansi.BOLD + ansi.UNDERLINE + f"{sum}" + ansi.END)
    return sum

def GradeRoll(roll):
    match roll:
        case value if 1 <= value <= 2:
            return ansi.RED
        case value if 3 <= value <= 4:
            return ansi.YELLOW
        case value if 5 <= value <= 6:
            return ansi.GREEN
        case _:
            return ''
        
def GradeTotal(total, numOfPlayers):
    low = numOfPlayers * 2
    med = (numOfPlayers * 6) - low
    match total:
        case value if 1 <= value <= low:
            return ansi.RED
        case value if low <= value <= med:
            return ansi.YELLOW
        case value if value >= med:
            return ansi.GREEN
        case _:
            return ''