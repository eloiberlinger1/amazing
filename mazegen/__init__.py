from .models import MazeCell
from .render import MazeRender
from .main import MazeGenerator, MazeManager
from .shortest_path import BFS

__all__ = ["MazeCell", "MazeManager", "MazeRender", "BFS"]
__version__ = "1.0.0"
__author__ = "Eloi Berlinger, Weijia Han"
