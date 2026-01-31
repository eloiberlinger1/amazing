#!/usr/bin/env python3
"""
Docstring pour a_maze_ing
"""

from config_loader import get_config
import sys
import os
import termios
import tty
from mazegen import MazeManager, BFS


def get_input():
    """Get a single character from stdin without requiring Enter"""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def clear_screen():
    """Clear the terminal screen"""
    os.system("clear" if os.name != "nt" else "cls")


def print_banner():
    """Print the ASCII banner"""
    print("\n\n\n\n\n")
    print(
        (
            "   ░███         ░███     ░███    ░███    ░█████████ "
            "░██████████     ░██████░███    ░██   ░██████\n"
            "  ░██░██        ░████   ░████   ░██░██         ░██  "
            "░██               ░██  ░████   ░██  ░██   ░██\n"
            " ░██  ░██       ░██░██ ░██░██  ░██  ░██       ░██   "
            "░██               ░██  ░██░██  ░██ ░██\n"
            "░█████████      ░██ ░████ ░██ ░█████████    ░███    "
            "░█████████        ░██  ░██ ░██ ░██ ░██  █████\n"
            "░██    ░██      ░██  ░██  ░██ ░██    ░██   ░██      "
            "░██               ░██  ░██  ░██░██ ░██     ██\n"
            "░██    ░██      ░██       ░██ ░██    ░██  ░██       "
            "░██               ░██  ░██   ░████  ░██  ░███\n"
            "░██    ░██ ░███ ░██       ░██ ░██    ░██ ░█████████ "
            "░██████████ ░██ ░██████░██    ░███   ░█████░█"
        )
    )
    print("\nby wehan and eberling")
    print("\n\n\n\n")


def print_menu(show_path: bool, color_mode: str):
    """Print the interactive menu as an ASCII table"""
    path_status = "ON" if show_path else "OFF"
    color_status = color_mode

    menu = f"""
                    A-MAZE-ING MENU
----------------------------------------------------------
  [1] Generate maze
  [2] Show / Hide shortest path  [{path_status}]
  [3] Change colors
      └─ Current mode: {color_status}
  [Q] Quit
----------------------------------------------------------

Press a key: """
    print(menu, end="", flush=True)


def print_color_submenu():
    """Print the color selection submenu"""
    menu = """
                    COLOR SELECTION MENU
----------------------------------------------------------
  [1] Default (no colors)
  [2] Color maze walls
  [3] Color only 42 pattern
  [B] Back to main menu
----------------------------------------------------------

Press a key: """
    print(menu, end="", flush=True)


def generate_maze(config):
    """Generate a new maze"""
    mm = MazeManager(config)
    mm.generate_maze_dfs()
    return mm


def calculate_path(mm: MazeManager):
    """Calculate the shortest path for the maze"""
    bfs = BFS()
    path = bfs.shortest_path(
        maze=mm.maze,
        height=mm.height,
        width=mm.width,
        start=mm.entry,
        end=mm.exit,
    )
    return path


def display_maze(mm: MazeManager, path: list = None, show_path: bool = True):
    """Display the maze with optional path"""
    if path is None:
        path = []
    if not show_path:
        path = []
    mm.print_maze(path)


def main():
    """
    Main entrypoint of the programm
    """
    print_banner()

    if len(sys.argv) >= 2:
        config_file = sys.argv[1]
    else:
        print("Correct usage: python3 a_maze_ing.py <config_file>")
        exit()

    config = get_config(config_file)

    # Initialize maze
    mm = MazeManager(config)
    mm.generate_maze_dfs()

    # Calculate initial path
    path = calculate_path(mm)

    # State variables
    show_path = True
    color_mode = "Default"

    # Main menu loop
    while True:
        clear_screen()
        print_banner()
        display_maze(mm, path, show_path)
        print_menu(show_path, color_mode)

        choice = get_input().upper()

        if choice == "1":
            # Generate new maze
            mm = generate_maze(config)
            path = calculate_path(mm)
            clear_screen()
            print_banner()
            display_maze(mm, path, show_path)

        elif choice == "2":
            # Toggle path visibility
            show_path = not show_path

        elif choice == "3":
            # Color selection submenu
            while True:
                clear_screen()
                print_banner()
                display_maze(mm, path, show_path)
                print_color_submenu()

                color_choice = get_input().upper()

                if color_choice == "1":
                    color_mode = "Default"
                    break
                elif color_choice == "2":
                    color_mode = "Maze walls"
                    break
                elif color_choice == "3":
                    color_mode = "42 pattern only"
                    break
                elif color_choice == "B":
                    break

        elif choice == "Q" or choice == "\x1b":  # Q or ESC
            clear_screen()
            print("\nGoodbye!\n")
            break


main()
