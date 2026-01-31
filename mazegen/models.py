from dataclasses import dataclass
from typing import Tuple


@dataclass
class MazeCell:
    """Represents a single cell in the maze"""

    north: bool
    south: bool
    east: bool
    west: bool
    forty_two_pattern: bool
    coordinates: Tuple[int, int]


if __name__ == "__main__":
    exit()
