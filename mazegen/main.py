"""
Docstring for mazegen.main
"""

from typing import Tuple, List, Dict
from dataclasses import dataclass
import random
from render import printmaze


@dataclass
class MazeCell:
    """Represents a single cell in the maze"""

    north: bool
    south: bool
    east: bool
    west: bool
    coordinates: Tuple[int, int]


class MazeManager:
    """Manages maze generation, storage and display operations"""

    def __init__(self, height: int, width: int, seed: int = None) -> None:
        self.height = height
        self.width = width

        self.maze = self.get_maze_container()
        self._cell_map = self._create_cell_map()

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

    def _create_cell_map(self) -> Dict[Tuple[int, int], MazeCell]:
        """
        Create a coordinate-to-cell mapping for fast lookup.
        Returns:Dictionary mapping (row, col) tuples to MazeCell objects
        """

        cell_map = {}
        for i in range(self.height):
            for j in range(self.width):
                cell = self.maze[i][j]
                cell_map[cell.coordinates] = cell
        return cell_map

    def get_maze_cell_from_coordinate(
        self, coordinate: Tuple[int, int]
    ) -> MazeCell:
        """Retrieve a MazeCell object using its coordinates."""

        try:
            return self._cell_map[coordinate]
        except KeyError:
            raise ValueError(f"{coordinate} does not exist")

    def get_all_coords(self) -> List[tuple[int, int]]:
        coords = []
        for row in self.maze:
            for cell in row:
                coords.append(cell.coordinates)
        return coords

    def get_neighbor_cells(
        self, current_cell: MazeCell, available: list[tuple[int, int]]
    ) -> Dict[str, MazeCell]:
        """Find neighboring cells that are available (not visited yet).

        Args:
            current_cell: The cell whose neighbors to check
            available: List of coordinates that haven't been visited yet

        Returns:
            Dictionary mapping direction strings ("north", ..., "west")
            to MazeCell objects that are unvisited neighbors
        """
        ava_neighbors = {}
        north = (current_cell.coordinates[0] - 1, current_cell.coordinates[1])
        south = (current_cell.coordinates[0] + 1, current_cell.coordinates[1])
        east = (current_cell.coordinates[0], current_cell.coordinates[1] + 1)
        west = (current_cell.coordinates[0], current_cell.coordinates[1] - 1)

        if north in available:
            ava_neighbors["north"] = self.get_maze_cell_from_coordinate(north)
        if south in available:
            ava_neighbors["south"] = self.get_maze_cell_from_coordinate(south)
        if east in available:
            ava_neighbors["east"] = self.get_maze_cell_from_coordinate(east)
        if west in available:
            ava_neighbors["west"] = self.get_maze_cell_from_coordinate(west)
        return ava_neighbors

    def generate_maze_dfs(self, seed: int = None) -> List[List[MazeCell]]:
        if seed is not None:
            random.seed(seed)
        # All cells start as unvisited
        available = self.get_all_coords()
        # Choose random starting point
        start_coord = random.choice(available)
        available.remove(start_coord)

        # Stack for DFS backtracking - holds the path we've taken
        stack = [start_coord]

        # DFS main loop - continue until all cells are visited
        while available:
            # Current position is the top of the stack
            current_coord = stack[-1]
            current_cell = self.get_maze_cell_from_coordinate(current_coord)
            ava_neighbors = self.get_neighbor_cells(current_cell, available)
            if not ava_neighbors:
                stack.pop()
                continue

            # choose random direction
            direction = random.choice(list(ava_neighbors.keys()))
            neighbor_cell = ava_neighbors[direction]

            # break the wall
            if direction == "north":
                current_cell.north = True
                neighbor_cell.south = True
            elif direction == "south":
                current_cell.south = True
                neighbor_cell.north = True
            elif direction == "east":
                current_cell.east = True
                neighbor_cell.west = True
            else:
                current_cell.west = True
                neighbor_cell.east = True

            # marked as visited
            available.remove(neighbor_cell.coordinates)
            # move to new position
            stack.append(neighbor_cell.coordinates)

        return self.maze

    def print_maze(self) -> None:
        """
        TEmporar function to pirnt the maze
        """
        myprintmaze = printmaze(self)
        print(myprintmaze)


def main():
    manager1 = MazeManager(6, 8, seed=123)
    manager1.generate_maze_dfs()
    manager1.print_maze()


if __name__ == "__main__":
    main()
