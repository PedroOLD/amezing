# a_maze_ing

Recursive Backtracking Maze Generation

This project uses the recursive backtracking algorithm to generate mazes. It’s a depth-first search (DFS) approach that creates a perfect maze (a maze with no loops and only one path between any two points).

The algorithm works as follows:

Start at an initial cell and mark it as visited.
Randomly select one of the neighboring cells that has not been visited yet.
Remove the wall between the current cell and the chosen neighbor.
Move to the neighbor cell and repeat the process recursively.
If a cell has no unvisited neighbors, backtrack to the previous cell and continue searching for unvisited neighbors.
The process ends when all cells in the grid have been visited.

Because the algorithm explores paths deeply before backtracking, it produces mazes with long corridors and fewer short dead ends, giving them a more organic and natural feel.