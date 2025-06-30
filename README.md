
# Maze Solver (Turtle Graphics Simulation)

This project simulates navigating a grid-based maze using different pathfinding algorithms.

Built with Python and `turtle`, the simulation visually demonstrates how each algorithm explores and solves the maze.

---

## Project Structure

- **main.py**  
  Runs the maze simulation with all three solvers. Visualizes their paths in different colors:  
  - Yellow: Flood Fill (uses a dynamic cost map)
  - Blue: BFS (shortest path)  
  - Green: DFS (non-optimal path)  
  - Red: Dead-End Solver (eliminates all dead ends)
  - Magenta: Dijkstra (uses a cost function)
  - Cyan: A* (uses Dijkstra with an additional heuristic for estimated distance)

- **maze.py**  
  Generates the grid and walls. Includes functions to add or remove walls and builds a complex maze with loops and decoys.

- **logic.py**  
  Contains the core logic for solvers:
  - `BFS`: Finds the shortest path.
  - `DFS`: Explores deeply and may find non-optimal paths.
  - `DeadEndSolver`: Fills dead ends to isolate the true path.
  - `FloodFill`: Finds the shortest path using a cost map.
  - `Dijkstra`: Finds the path using a cost function.
  - `AStar`: Finds the path using Dijkstra with an extra heuristic estimate.

- **drawers.py**  
  Defines the `Mouse` class used to draw the maze, walls, and animate the robot's movement on the grid.

---

## How to Run

Make sure Python is installed, then run:

```bash
python main.py
```

You'll see a visual simulation window. Each algorithm will take its turn solving the same maze.

---

## Requirements

- Python 3.9 or above
- No external libraries (uses built-in `turtle`)

---

