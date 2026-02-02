*This project has been created as part of the 42 curriculum by wehan and eberling.*
![Demo](https://filedn.eu/lqAABNUSgVkfRyevTm4sSpR/NEVER_DELETE_ALWAYS_ADD/Screencast%20from%2001-31-2026%2003_56_06%20PM.gif)

## Description

A-MAZE-ING is an interactive Python application for maze generation and solving. The project lets you create random mazes of various sizes, visualize the shortest path from entry to exit, and interact with the maze via an interactive menu.

The application can generate perfect mazes (without cycles) or imperfect mazes (with cycles), and has the option to include a "42" pattern visible in mazes large enough. The system uses hexadecimal encoding to represent the cell walls and automatically saves the generated maze and solution path to an output file.

## Features

- Generate random mazes using the DFS algorithm
- Visualize the shortest path using BFS
- Interactive menu system
- Color customization options
- Real-time maze display
- Support for perfect and imperfect mazes
- Automatic "42" pattern integration (for mazes ≥14×10)
- Hex-encoded wall representation
- Automatic file output including maze, entry/exit, and solution path

## Requirements

- Python 3
- Linux/Unix system (uses termios for input handling)

## Instructions

### Installation

1. Clone the repository or download the project files.

2. Install the dependencies (optional, for linting):
```bash
make install
```

Dependencies include `flake8` and `mypy` for linting and type checking.

### Basic Usage

Run the application with a configuration file:

```bash
python3 a_maze_ing.py <config_file>
```

Example:
```bash
python3 a_maze_ing.py config.txt
```

### Usage with Makefile

You can also use the Makefile:

```bash
make run config.txt
```

### Interactive Menu

Once the application is started, you have an interactive menu:

- **[1] Generate maze**: Generates a new maze using the configuration file parameters
- **[2] Show / Hide shortest path**: Shows or hides the shortest path (ON/OFF)
- **[3] Change colors**: Change maze display color
  - Default (no color)
  - Red
  - Green
  - Yellow
- **[Q] Quit**: Quit the application (or press ESC)

### Configuration File

The config file should follow this structure:

```
# mandatory
WIDTH=50
HEIGHT=20
ENTRY=0,1
EXIT=10,14
OUTPUT_FILE=maze.txt
PERFECT=True
#SEED=42
```

#### Full config file structure

- **WIDTH** (required): Maze width in number of cells (positive integer)
- **HEIGHT** (required): Maze height in number of cells (positive integer)
- **ENTRY** (required): Entry coordinates as `row,column` (tuple of integers)
- **EXIT** (required): Exit coordinates as `row,column` (tuple of integers)
- **OUTPUT_FILE** (required): Name of the output file where the maze will be saved
- **PERFECT** (required): `True` for a perfect maze (no cycles), `False` for imperfect maze (with cycles)
- **SEED** (optional): Seed for random generation (integer). If missing or commented, generation is non-deterministic
- **COLOR** (optional, handled via interface): Display color (Default, Red, Green, Yellow)

**Important notes:**
- Lines starting with `#` are comments
- ENTRY and EXIT coordinates must be valid (within the maze bounds)
- ENTRY and EXIT cannot be identical
- Coordinates are zero-indexed

### Output Format

The output file contains:
1. **Maze grid**: Each line represents a row of cells, each hexadecimal character represents the walls of a cell
   - `0` = no walls open
   - `1` = north wall open
   - `2` = east wall open
   - `3` = north and east walls open
   - `4` = south wall open
   - `5` = north and south walls open
   - `6` = east and south walls open
   - `7` = north, east and south walls open
   - `8` = west wall open
   - `9` = north and west walls open
   - `a` = east and west walls open
   - `b` = north, east and west walls open
   - `c` = south and west walls open
   - `d` = north, south and west walls open
   - `e` = east, south and west walls open
   - `f` = all walls open
2. **Empty line**
3. **ENTRY**: Entry coordinates in the format `row,column`
4. **EXIT**: Exit coordinates in the format `row,column`
5. **Solution path**: Sequence of directions (N, E, S, W) for the shortest path

### Makefile Commands

- `make install`: Creates a virtual environment and installs dependencies
- `make run <config_file>`: Runs the application with the given configuration file
- `make lint`: Runs flake8 and mypy to check the code
- `make lint-strict`: Runs mypy in strict mode and flake8
- `make debug <config_file>`: Runs the application in debug mode with pdb
- `make clean`: Removes cache files and the virtual environment
- `make re`: Cleans and reinstalls the environment

## Maze Generation Algorithm

### Chosen Algorithm: Depth-First Search (DFS)

The project uses the **Depth-First Search (DFS)** algorithm with backtracking to generate mazes.

#### Why this choice?

1. **Simplicity and efficiency**: DFS is simple to implement and very effective for generating perfect mazes (without cycles).

2. **Connectedness guarantee**: DFS ensures there is a unique path between any pair of cells in a perfect maze, which is desirable.

3. **Structure control**: Using a stack allows precise control over the generation process and makes implementing backtracking easy.

4. **Performance**: Time complexity is O(n) where n is the number of cells, which is optimal for this problem type.

5. **Flexibility**: The algorithm can easily be extended to create imperfect mazes by adding extra openings after the initial generation.

#### Operation

1. **Initialization**: All cells are initially closed (all walls present).

2. **Starting point**: A random starting cell is chosen in the maze.

3. **DFS Exploration**:
   - The current cell is marked as visited
   - Unvisited neighbors are identified
   - A random neighbor is chosen
   - The wall between the current cell and the chosen neighbor is removed
   - The neighbor becomes the new current cell and is added to the stack
   - If no neighbor is available, backtrack by popping from the stack

4. **Imperfect maze**: If `PERFECT=False`, additional openings are made in dead-ends (cells with 3 walls) to create cycles.

5. **42 pattern**: If the maze is big enough (≥14×10), a "42" pattern is added by marking certain cells as inaccessible.

### Solution Algorithm: Breadth-First Search (BFS)

To find the shortest path, the project uses **Breadth-First Search (BFS)**.

#### Why BFS

- BFS guarantees to find the shortest path in an unweighted graph
- Using a queue ensures all paths of length k are explored before those of k+1
- Complexity O(n) where n is the number of cells

## Resources

### References

- **Maze generation algorithms**: Documentation on DFS and backtracking for maze generation
- **Breadth-First Search**: Graph traversal algorithms for maze solving
- **Hexadecimal encoding**: System for cell wall representation (4 bits: north, east, south, west)
- **Termios (Python)**: Docs for non-blocking keyboard input handling on Linux/Unix

### Use of AI

AI was used for:
- **Development assistance**: Help with code structure and bug-solving
- **Documentation**: Generating docstrings and explanatory comments
- **Testing and validation**: Checking algorithm logic
- **Optimization**: Suggestions for better performance and readability
- **Redaction**: Writing this elegant georgerous beautifull amazing README file.

## Team management & planning

### Task distribution

- **wehan**:
  - DFS algorithm implementation for maze generation
  - 42 pattern and imperfect maze management
  - Hex encoding and output file save
  - BFS algorithm implementation for shortest path


- **eberling**:
  - Interactive menu and user input management
  - Config file loading and validation
  - Color integration and display customization
  - Maze rendering system and display
### Project planning

1. **Phase 1 - Base structure**:
   - Define project structure and data models
   - Implement `MazeCell` and basic maze structure

2. **Phase 2 - Generation**:
   - Implement DFS algorithm
   - Handle perfect and imperfect mazes
   - Integrate the 42 pattern

3. **Phase 3 - Solving**:
   - Implement BFS for shortest path
   - Convert path to directions (N, E, S, W)

4. **Phase 4 - User interface**:
   - Develop the interactive menu
   - Handle non-blocking keyboard input
   - Color system and customization

5. **Phase 5 - Config and output**:
   - Config file parser
   - Parameter validation
   - Hex encoding and file output

6. **Phase 6 - Finalization**:
   - Testing and debugging
   - Documentation and README
   - Optimization and code cleanup

### Development tools

- **Version control**: Git for version management
- **Linting**: flake8 for code style checks
- **Type checking**: mypy for type verification
- **Virtual environment**: venv for dependency isolation
- **Makefile**: Automate common tasks

## Authors

by wehan and eberling
