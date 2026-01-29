#!/usr/bin/env python3
"""
Docstring pour a_maze_ing
"""

from config_loader import get_config
import sys
import mazegen


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
    mazegen.print_maze(int(config["WIDTH"]), int(config["HEIGHT"]))


main()
