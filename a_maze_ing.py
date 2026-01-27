#!/usr/bin/env python3
"""
Docstring pour a_maze_ing
"""

import sys
import mazegen


def load_config(file_path: str) -> dict[str, str]:
    """
    Load configuration file
    """
    config_data: dict[str, str] = {}
    try:
        with open(file_path, "r") as f:
            for li in f:
                li = li.strip()
                if "=" in li:
                    li = li.split("=", 1)
                    key = li[0]
                    config_data[key] = li[1]
    except Exception:
        print("File not found")

    return config_data


def main():
    """
    Docstring pour main
    """

    # get config values
    if len(sys.argv) >= 2:
        config_file = sys.argv[1]
    else:
        print("Correct usage: python3 a_maze_ing.py <config_file>")
        exit()
    config = load_config(config_file)
    print(config)
    mazegen.print_maze(int(config["WIDTH"]), int(config["HEIGHT"]))


main()
