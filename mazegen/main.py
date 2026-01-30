"""
Docstring for mazegen.main
"""

from models import MazeCell
from typing import Tuple, List, Dict
from render import MazeRender
import random
from shortest_path import BFS


class MazeManager:
    """Manages maze generation, storage and display operations"""

    def __init__(
        self, height: int, width: int, seed: int = None, perfect: bool = True
    ) -> None:
        self.height = height
        self.width = width
        self.seed = seed
        self.perfect = perfect

        self.rng = random.Random(seed)

        # 42 pattern coords (may be empty if maze too small)
        self.pattern_coordinates: List[Tuple[int, int]] = (
            self.get_pattern_coords()
            if self.check_42_pattern_availability()
            else []
        )

        self.maze = self.get_maze_container()
        self._cell_map = self._create_cell_map()

    def check_42_pattern_availability(self) -> bool:
        if int(self.width) >= 14 and int(self.height) >= 10:
            return True
        print("The maze size too small, 42 pattern omitted!")
        return False

    def get_pattern_coords(self) -> List[Tuple[int, int]]:
        """
        Returns coordinates that draw a visible 42 using fully closed cells.
        Pattern is centered in the maze.
        """

        coords: List[Tuple[int, int]] = []
        r, c = (int((self.height - 5) / 2)), int((self.width - 7) / 2)

        # "4" part
        coords.append((r, c))
        coords.append((r + 1, c))
        coords.append((r + 2, c))
        coords.append((r + 2, c + 1))
        coords.append((r + 2, c + 2))
        coords.append((r + 3, c + 2))
        coords.append((r + 4, c + 2))

        # "2" part
        coords.append((r, c + 4))
        coords.append((r + 2, c + 4))
        coords.append((r + 3, c + 4))
        coords.append((r + 4, c + 4))
        coords.append((r, c + 5))
        coords.append((r + 2, c + 5))
        coords.append((r + 4, c + 5))
        coords.append((r, c + 6))
        coords.append((r + 1, c + 6))
        coords.append((r + 2, c + 6))
        coords.append((r + 4, c + 6))

        return coords

    def get_maze_container(self) -> List[List[MazeCell]]:
        """Initializes the grid with closed cells."""

        container = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                if tuple([i, j]) in self.pattern_coordinates:
                    row.append(
                        MazeCell(
                            False,
                            False,
                            False,
                            False,
                            True,
                            (i, j),
                        )
                    )
                else:
                    row.append(
                        MazeCell(
                            False,
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
        ava_neighbors: Dict[str, MazeCell] = {}
        r, c = current_cell.coordinates
        north = (r - 1, c)
        south = (r + 1, c)
        east = (r, c + 1)
        west = (r, c - 1)

        if north in available:
            ava_neighbors["north"] = self.get_maze_cell_from_coordinate(north)
        if south in available:
            ava_neighbors["south"] = self.get_maze_cell_from_coordinate(south)
        if east in available:
            ava_neighbors["east"] = self.get_maze_cell_from_coordinate(east)
        if west in available:
            ava_neighbors["west"] = self.get_maze_cell_from_coordinate(west)
        return ava_neighbors

    def make_imperfect(self) -> None:
        """
        Add extra openings to create loops (non-perfect maze)
        Note: it does not guarantee another well-looped path
        """
        threshold = 0.35

        for row in self.maze:
            for cell in row:
                # jump over coordinates in 42 pattern
                if cell.coordinates in self.pattern_coordinates:
                    continue
                r, c = cell.coordinates

                # walls show the blocked side(s) of a cell
                walls = []
                if not cell.north:
                    walls.append("north")
                if not cell.south:
                    walls.append("south")
                if not cell.east:
                    walls.append("east")
                if not cell.west:
                    walls.append("west")

                # Only target dead-ends (3 blocked walls)
                # to keep changes small and controlled.
                if len(walls) != 3:
                    continue

                # remove candidate wall directions that point outside the maze
                if r == 0 and "north" in walls:
                    # r == 0 is the rule to avoid breaking
                    # the outside north border wall
                    # "north" in walls for remove() to avoid reporting an error
                    walls.remove("north")
                if c == 0 and "west" in walls:
                    walls.remove("west")
                    # height = row number of coordinates
                    # width = cell/column number of coordinates
                    # r: 0..height-1 (row index)
                    # c: 0..width-1  (col index)
                if r == self.height - 1 and "south" in walls:
                    walls.remove("south")
                if c == self.width - 1 and "east" in walls:
                    walls.remove("east")

                # remove 42-pattern-nearby cell directions that point to 42
                # ensure 42 border block and cells one step back nearby
                # have the same blocked status
                # for the shared wall

                if (r - 1, c) in self.pattern_coordinates and "north" in walls:
                    walls.remove("north")
                if (r + 1, c) in self.pattern_coordinates and "south" in walls:
                    walls.remove("south")
                if (r, c - 1) in self.pattern_coordinates and "west" in walls:
                    walls.remove("west")
                if (r, c + 1) in self.pattern_coordinates and "east" in walls:
                    walls.remove("east")

                if not walls:
                    continue

                if self.rng.random() > threshold:
                    continue

                choice = self.rng.choice(walls)

                if choice == "north":
                    cell.north = True
                    self.get_maze_cell_from_coordinate((r - 1, c)).south = True
                elif choice == "south":
                    cell.south = True
                    self.get_maze_cell_from_coordinate((r + 1, c)).north = True
                elif choice == "east":
                    cell.east = True
                    self.get_maze_cell_from_coordinate((r, c + 1)).west = True
                elif choice == "west":
                    cell.west = True
                    self.get_maze_cell_from_coordinate((r, c - 1)).east = True

    def generate_maze_dfs(self, seed: int = None) -> List[List[MazeCell]]:
        if seed is not None:
            self.rng.seed(seed)
        # All cells start as unvisited
        available = self.get_all_coords()

        # remove 42 pattern from DFS available list[tuples]
        for coord in self.pattern_coordinates:
            if coord in available:
                available.remove(coord)

        if not available:
            return self.maze

        # Choose random starting point
        start_coord = self.rng.choice(available)
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
            direction = self.rng.choice(list(ava_neighbors.keys()))
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
            # pushed to previous path stacks end
            stack.append(neighbor_cell.coordinates)

        if not self.perfect:
            self.make_imperfect()
        return self.maze

    def print_maze(self) -> None:
        """
        TEmporar function to pirnt the maze
        """
        renderer = MazeRender(
            entry=(0, 0), exit=(self.height - 1, self.width - 1)
        )
        myprintmaze = renderer.render(self)
        print(myprintmaze)


def main():
    manager1 = MazeManager(15, 20, seed=123, perfect=False)
    manager1.generate_maze_dfs()

    bfs = BFS()
    start = (0, 0)
    end = (manager1.height - 1, manager1.width - 1)
    manager1.print_maze()

    path = bfs.shortest_path(
        maze=manager1.maze,
        height=manager1.height,
        width=manager1.width,
        start=start,
        end=end
    )

    print("BFS path:", path)
    renderer = MazeRender(entry=start, exit=end)
    print(renderer.render(manager1, path=path))


if __name__ == "__main__":
    main()

# seed()      → 决定“随机序列长什么样”
# random()   → 从这个序列里取下一个 0~1 的数

# Status Summary (Submission Notes)
# [DONE]
# DFS maze generation (seeded, PERFECT / imperfect)
# Wall consistency (N / E / S / W)
# 42 pattern handled
# BFS shortest path algorithm works
# [TO DO]
# !!! Config → program integration
# 1.1 Parse WIDTH, HEIGHT, ENTRY, EXIT, OUTPUT_FILE, PERFECT, SEED
# 1.2 Convert ENTRY/EXIT from x,y to (row,col)
# 1.3 Remove hard-coded values
# !!! Output file
# 2.1 Hex wall encoding
# 2.2 Write maze grid to OUTPUT_FILE
# 2.3 Append ENTRY, EXIT, shortest path (N/E/S/W)
# !!! 3×3 open area rule
# 3.1 Detect 3×3 open areas
# 3.2 Regenerate maze if invalid
