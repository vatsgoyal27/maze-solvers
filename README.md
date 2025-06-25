
# Maze Solver (Turtle Graphics Simulation)(WIP)

This project simulates navigating a grid-based maze using three different pathfinding algorithms: **Breadth-First Search (BFS)**, **Depth-First Search (DFS)**, and **Dead-End Filling**.

Built with Python and `turtle`, the simulation visually demonstrates how each algorithm explores and solves the maze.

---

## Project Structure

- **main.py**  
  Runs the maze simulation with all three solvers. Visualizes their paths in different colors:  
  - Blue: BFS (shortest path)  
  - Green: DFS (non-optimal path)  
  - Red: Dead-End Solver (eliminates all dead ends)

- **maze.py**  
  Generates the grid and walls. Includes functions to add or remove walls and builds a complex maze with loops and decoys.

- **logic.py**  
  Contains the core logic for three solvers:
  - `BFS`: Finds the shortest path.
  - `DFS`: Explores deeply and may find non-optimal paths.
  - `DeadEndSolver`: Fills dead ends to isolate the true path.

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

## To-Do

- Add more maze solving algorithms (eg: A*, Dijkstra, Floodfill)

---

