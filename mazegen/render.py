"""
Print the maze

"""

from typing import List


def printmaze(mazemanager) -> str:
    """
    Docstring for printmaze
    """
    maze = mazemanager.maze

    # Tuple: (north, south, east, west)
    chars = {
        (1, 1, 0, 0): "│",  # : Nord + Sud
        (0, 0, 1, 1): "─",  # Est + Ouest
        (1, 0, 1, 0): "╰",  # Nord + Est
        (1, 0, 0, 1): "╯",  # Nord + Ouest
        (0, 1, 1, 0): "╭",  # Sud + Est
        (0, 1, 0, 1): "╮",  # Sud + Ouest
        (1, 1, 1, 1): "┼",  # Nord + Sud + Est + Ouest
    }

    caneva = List[List[str]]

    for i in range(((mazemanager.height * 2) + 1)):

# demo
#
# ╭─╮
# │ │
# ╰─╯
#

        line = []

        for j in range((mazemanager.width * 2) + 1):
            if (i % 2 == 0):
            line.append(chars[maze[i][j].coordinates])

        caneva.append(line)

    for line in maze:

        l1, l2, l3 = "", "", ""

        for c in line:

            content = "   "
            if c.coordinates == (0, 0):
                content = " S "
            elif c.coordinates == (14, 19):
                content = " E "
            elif c.coordinates == "solution":
                content = " • "

            l1 += "╭───╮" if not c.north else "|   |"
            l2 += (
                ("|" if not c.west else " ")
                + content
                + ("|" if not c.east else " ")
            )
            l3 += "╰───╯" if not c.south else "|   |"

        return_str += l1 + "\n" + l2 + "\n" + l3 + "\n"

    return str(return_str)


if __name__ == "__main__":
    printmaze(None)
