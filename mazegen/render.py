"""
Print the maze

"""

from typing import Protocol, Tuple, List
from .models import MazeCell


class MazeManagerProtocol(Protocol):
    """
    Minimal expected MazeManager to process rendering
    """

    height: int
    width: int
    maze: list[list[MazeCell]]


class MazeRender:

    WALL_CHARS = {
        (1, 1, 0, 0): "╰",
        (0, 0, 1, 1): "╮",
        (1, 0, 1, 0): "│",
        (1, 0, 0, 1): "╯",
        (0, 1, 1, 0): "╭",
        (1, 0, 0, 0): "│",
        (0, 0, 1, 0): "│",
        (0, 1, 0, 1): "─",
        (0, 0, 0, 1): "─",
        (0, 1, 0, 0): "─",
        (1, 0, 1, 1): "┤",
        (1, 1, 0, 1): "┴",
        (0, 1, 1, 1): "┬",
        (1, 1, 1, 0): "├",
        (1, 1, 1, 1): "┼",
    }

    def __init__(
        self, o_file: str, entry: tuple[int, int], exit: tuple[int, int]
    ):
        """Initialize Maze renderer with entry and exit points"""
        self.entry = entry
        self.exit = exit

        self.height = 0
        self.width = 0
        self.canevas_h = 0
        self.canevas_w = 0

        self.o_file = o_file

    def _get_canevas(self, h: int, w: int) -> list[list[bool]]:
        """
        Docstring for _get_canva
        """
        c_h = self.canevas_h
        c_w = self.canevas_w

        canevas = [[True for _ in range(c_w)] for _ in range(c_h)]

        for r in range(h):
            for c in range(w):
                cell = self.maze[r][c]

                caneva_r = (r * 2) + 1
                caneva_c = (c * 2) + 1

                canevas[caneva_r][caneva_c] = False

                if cell.north:
                    canevas[caneva_r - 1][caneva_c] = False
                if cell.south:
                    canevas[caneva_r + 1][caneva_c] = False
                if cell.east:
                    canevas[caneva_r][caneva_c + 1] = False
                if cell.west:
                    canevas[caneva_r][caneva_c - 1] = False

        return canevas

    def _write_maze_file(self, f):

        final_content: List[str] = []

        for line in self.maze:
            line_str = ""
            for cell in line:

                # 1 = 0001 in binary
                # 2 = 0010 in binary
                # 4 = 0100 in binary
                # 8 = 1000 in binary

                value = 0
                if cell.north:
                    value |= 1
                if cell.east:
                    value |= 2
                if cell.south:
                    value |= 4
                if cell.west:
                    value |= 8

                # >>> hex(5) -> '0x5'
                # >>> hex(5)[-1] -> '5'
                line_str += str(hex(value)[-1])

            final_content.append(str(line_str))

        for li in final_content:
            f.write(li + "\n")

    def save_maze_file(self) -> None:

        with open(self.o_file, "w") as file:
            self._write_maze_file(file)

    def render(
        self,
        generated_maze: MazeManagerProtocol,
        path: List[Tuple[int, int]],
    ) -> str:
        """
        Docstring for printmaze
        """
        self.maze = generated_maze.maze
        self.height = generated_maze.height
        self.width = generated_maze.width
        self.canevas_h = (self.height * 2) + 1
        self.canevas_w = (self.width * 2) + 1

        canevas = self._get_canevas(
            generated_maze.height, generated_maze.width
        )

        # ====================
        #    Integer char
        # ====================

        c_h = self.canevas_h
        c_w = self.canevas_w
        res = ""

        for r in range(c_h):
            line_str = ""
            for c in range(c_w):

                if canevas[r][c]:
                    n = r > 0 and canevas[r - 1][c]
                    s = r < c_h - 1 and canevas[r + 1][c]
                    w = c > 0 and canevas[r][c - 1]
                    e = c < c_w - 1 and canevas[r][c + 1]

                    char = self.WALL_CHARS.get(
                        (int(n), int(e), int(s), int(w)), "┼"
                    )
                    line_str += char + ("─" if e else " ")
                else:
                    content = " "
                    # Center of element
                    if r % 2 != 0 and c % 2 != 0:
                        mr, mc = (r - 1) // 2, (c - 1) // 2

                        # Coords in original mze
                        if (mr, mc) == self.entry:
                            content = "S"

                        elif (mr, mc) == self.exit:
                            content = "E"

                        # add shortest path
                        elif (mr, mc) in path:
                            content = "·"

                    line_str += content + " "
            res += line_str + "\n"

        self.save_maze_file()

        return str(res)


if __name__ == "__main__":
    exit()
