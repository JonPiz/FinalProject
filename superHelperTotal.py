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