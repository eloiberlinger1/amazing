#!/usr/bin/env python3
"""
Docstring pour a_maze_ing
"""

from config_loader import get_config
import sys
from mazegen import MazeManager


def main():
    """
    Main entrypoint of the programm
    """

    if len(sys.argv) >= 2:
        config_file = sys.argv[1]
    else:
        print("Correct usage: python3 a_maze_ing.py <config_file>")
        exit()

    config = get_config(config_file)
    print(config)
    # mm = MazeManager(15, 20, seed=123)
    mm = MazeManager(config)
    mm.generate_maze_dfs()
    mm.print_maze()


main()
