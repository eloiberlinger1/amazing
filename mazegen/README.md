*This project has been created as part of the 42 curriculum by wehan and eberling.*

## `mazegen` module

The `mazegen` package is designed to be reusable in other projects. It includes:

- **`MazeManager`** (`mazegen/main.py`): Main class for managing maze generation and manipulation
- **`MazeCell`** (`mazegen/models.py`): Data model to represent a maze cell
- **`BFS`** (`mazegen/shortest_path.py`): Class to compute the shortest path
- **`MazeRender`** (`mazegen/render.py`): Class for rendering and displaying mazes

### How to use the module in another project

1. **Import:**
```python
from mazegen import MazeManager, BFS
from mazegen.models import MazeCell
from mazegen.render import MazeRender
```

2. **Maze creation:**
```python
config = {
    "WIDTH": 20,
    "HEIGHT": 10,
    "ENTRY": (0, 1),
    "EXIT": (9, 18),
    "OUTPUT_FILE": "my_maze.txt",
    "PERFECT": True,
    "SEED": 42,
    "COLOR": "Default"
}

mm = MazeManager(config)
mm.generate_maze_dfs()
```

3. **Compute shortest path:**
```python
bfs = BFS()
path = bfs.shortest_path(
    maze=mm.maze,
    height=mm.height,
    width=mm.width,
    start=mm.entry,
    end=mm.exit
)
```

4. **Display the maze:**
```python
mm.print_maze(path)
```

5. **Access data:**
```python
# Access a specific cell
cell = mm.get_maze_cell_from_coordinate((5, 5))

# Get all available neighbors of a cell
neighbors = mm.get_neighbor_cells(cell, available_coords)
```

### Standalone usage example

```python
from config_loader import get_config
from mazegen import MazeManager, BFS

# Load the configuration
config = get_config("config.txt")

# Create and generate the maze
maze_manager = MazeManager(config)
maze_manager.generate_maze_dfs()

# Compute the path
bfs = BFS()
path = bfs.shortest_path(
    maze=maze_manager.maze,
    height=maze_manager.height,
    width=maze_manager.width,
    start=maze_manager.entry,
    end=maze_manager.exit
)

# Display
maze_manager.print_maze(path)
```
