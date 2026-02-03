from dataclasses import dataclass
from typing import Tuple, Dict
import random


@dataclass
class MazeCell:
    """Represents a single cell in the maze"""

    north: bool = False
    south: bool = False
    east: bool = False
    west: bool = False
    forty_two_pattern: bool = False
    coord: Tuple[int, int] = (0, 0)


def create_cell_map(w, h, maze) -> Dict[Tuple[int, int], MazeCell]:
    """
    Create a coordinate-to-cell mapping for fast lookup.
    Returns:Dictionary mapping (row, col) tuples to MazeCell objects
    """

    cell_map = {}
    for i in range(h):
        for j in range(w):
            cell = maze[i][j]
            cell_map[cell.coord] = cell
    return cell_map


def get_maze():

    w = 10
    h = 10

    mazecells = [[MazeCell(coord=(r, c)) for c in range(w)] for r in range(h)]

    cell_map: Dict[Tuple[int, int], MazeCell] = create_cell_map(
        w, h, mazecells
    )

    for r in mazecells:
        for c in mazecells:
            print("x", end="")
        print()

    start = (0, 0)
    visited = {start}
    path = [start]

    while path:
        current = path[-1]

        r, c = current


get_maze()

if __name__ == "__main__":
    exit()
