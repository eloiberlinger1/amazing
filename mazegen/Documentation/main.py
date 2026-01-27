"""
Docstring for mazegen.main
"""

from typing import Tuple, List
from dataclasses import dataclass


class MazeGenerator:
    def __init__(self):
        print("def")


@dataclass
class MazeCell:
    north: bool
    south: bool
    east: bool
    west: bool
    coord: Tuple[int, int]


class MazeManager:

    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width
        self.elmts = {
            "h": "─",
            "v": "│",
            "c1": "╭",
            "c2": "╰",
            "c3": "╮",
            "c4": "╯",
            "f": "▒",
        }

    def get_maze_container(self) -> List[List[MazeCell]]:
        """Initializes the grid with closed cells."""
        container = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(
                    MazeCell(
                        False,
                        False,
                        False,
                        False,
                        (i, j),
                    )
                )
            container.append(row)

        return container


def print_maze(width: int, height: int) -> None:
    """
    Docstring for print_maze
    """

    print("asd")

    generator = MazeManager(width, height)

    maze = generator.get_maze_container()

    for l in maze:
        for i in l:
            print(i, end="")
        print()


if __name__ == "__main__":
    print_maze()
