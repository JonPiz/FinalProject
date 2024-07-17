import helperDice as HD
from ansi import ansi

def StyleTotal(total, totalPlayers):
    return (
        f"{ansi.BOLD}"
        f"{ansi.UNDERLINE}"
        f"{HD.GradeTotal(total, totalPlayers)}"
        f"{total}"
        f"{ansi.END}"
    )

def StyleFirstPlayer(sPlayers):
    return (
        f"{ansi.BOLD}"
        f"{ansi.UNDERLINE}"
        f"{sPlayers[0][0]}"
        f"{ansi.END}"
    )