"""
Print the maze

"""


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

    return_str = ""

    for line in maze:
        for c in line:
            wall_i = (int(c.north), int(c.south), int(c.east), int(c.west))
            caracter = chars.get(wall_i, "?")

            return_str += caracter
        return_str += "\n"

    return str(return_str)


if __name__ == "__main__":
    printmaze(None)
