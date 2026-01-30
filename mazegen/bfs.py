from collections import deque
from typing import Deque, Dict, List, Optional, Tuple
from models import MazeCell


class BFS:
    """
    Breadtg-First Search
    There may be multiple shortest paths,
    but BFS returns the first one discovered according to the FIFO principle.
    """

    def pathfind(
      self,
      maze: List[List[MazeCell]],
      height: int,
      width: int,
      start: Tuple[int, int],
      end: Tuple[int, int]
    ) -> Optional[List[Tuple[int, int]]]:
        if height <= 0 or width <= 0:
            return None
        if not self._in_bounds(start, height, width):
            return None
        if not self._in_bounds(end, height, width):
            return None
        if maze[start[0]][start[1]].forty_two_pattern:
            return None
        if maze[start[0]][start[1]].forty_two_pattern:
            return None

        queue: Deque[Tuple[int, int]] = deque([start])
        parent: Dict[Tuple[int, int], Tuple[int, int] | None] = {start: None}

        while queue:
            cur = queue.popleft()
            if cur == end:
                return self._reconstruct_path(parent, end)

            for neighbor in self._neighbors(cur, maze, height, width):
                if neighbor not in parent:
                    parent[neighbor] = cur  # visited
                    queue.append(neighbor)

        return None

    def path_to_directions(self, path: List[Tuple[int, int]]) -> List[str]:
        """Convert a path of coordinates
        to a list of directions (N, E, S, W)"""

        if len(path) < 2:
            return []

        directions: list[str] = []
        for i in range(len(path) - 1):
            current: tuple[int, int] = path[i]
            next_pos: tuple[int, int] = path[i + 1]
            row_diff: int = next_pos[0] - current[0]  # -1 up, 1 down
            col_diff: int = next_pos[i] - current[1]  # -1 left, 1 right
            if row_diff == -1:
                directions.append("N")
            elif row_diff == 1:
                directions.append("S")
            elif col_diff == -1:
                directions.append("W")
            elif col_diff == 1:
                directions.append("E")
        return directions

# ----------helpers---------------

    def _in_bounds(self, pos: Tuple[int, int], h: int, w: int) -> bool:
        r, c = pos
        return 0 <= r < h and 0 <= c < w

    def _reconstruct_path(
        self,
        parent: Dict[Tuple[int, int], Tuple[int, int] | None],
        end: Tuple[int, int]
    ) -> List[Tuple[int, int]]:
        path: List[Tuple[int, int]] = []
        node: Tuple[int, int] | None = end
        while node is not None:
            path.append(node)
            node = parent[node]
        path.reverse()
        return path

    def _neighbors(
        self,
        cur: Tuple[int, int],
        maze: List[List[MazeCell]],
        h: int,
        w: int
    ) -> List[Tuple[int, int]]:
        r, c = cur
        cur_cell = maze[r][c]
        neighbors: List[Tuple[int, int]] = []

        # if north-side wall open & x north border wall &  x 42 pattern
        if (
            cur_cell.north and r > 0 and
            not maze[r - 1][c].forty_two_pattern
        ):
            neighbors.append((r - 1, c))
        if (
            cur_cell.south and r < h - 1 and
            not maze[r + 1][c].forty_two_pattern
        ):
            neighbors.append((r + 1, c))
        if (
            cur_cell.west and c > 0 and
            not maze[r][c - 1].forty_two_pattern
        ):
            neighbors.append((r, c - 1))
        if (
            cur_cell.east and c < w - 1 and
            not maze[r][c + 1].forty_two_pattern
        ):
            neighbors.append((r, c + 1))

        return neighbors
