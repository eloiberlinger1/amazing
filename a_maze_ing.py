#!/usr/bin/env python3
"""
Docstring pour a_maze_ing
"""


def load_config(file_path: str) -> dict[str, str]:
    """
    Load configuration file
    """
    config_data: dict[str, str] = {}
    with open(file_path, "r") as f:
        for li in f:
            li = li.strip()
            if "=" in li:
                li = li.split("=", 1)
                key = li[0]
                config_data[key] = li[1]

    return config_data


def main():
    """
    Docstring pour main
    """
    print("Amazing")

    # get config values
    config = load_config("config.txt")
    print(config)


main()
