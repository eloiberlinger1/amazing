"""
Docstring for mazegen.main
"""


class MazeGenerator:
    def __init__(self):
        print("def")


class MazeCell:
    north: bool
    south: bool
    east: bool
    west: bool


def print_maze(width: int, height: int) -> None:
    """
    Docstring for print_maze
    """

    print("asd")

    walls = {
        "h": "─",
        "v": "│",
        "c1": "╭",
        "c2": "╰",
        "c3": "╮",
        "c4": "╯",
        "f": "▒",
    }

    maze = [[MazeCell() for j in range(width)] for i in range(height)]
    for j in maze:
        for i in j:
            print(walls["v"], end="")
        print()


if __name__ == "__main__":
    print_maze()
