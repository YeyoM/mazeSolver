import time

# Utils
from utils.generate_grid import generate_grid
from utils.print_maze import print_maze
from utils.carve import carve
from utils.modify import modify

# Algorithms
from algorithms.dfs_maze_solver import dfs_maze_solver
from algorithms.bfs_maze_solver import bfs_maze_solver
from algorithms.dijkstra_maze_solver import dijkstra_maze_solver
from algorithms.astar_maze_solver import astar_maze_solver

def main():

  m = 41
  n = 41
  maze = []

  maze = generate_grid(n, m, maze)
  carve(maze)
  modify(maze, m, n)

  maze_for_dfs = maze.copy()
  maze_for_bfs = maze.copy()
  maze_for_dijkstra = maze.copy()
  maze_for_astar = maze.copy()
 
  start_time_dfs = time.time()
  dfs_maze_solver(maze_for_dfs, [1, 1], [m-2, n-2])
  print("Execution time DFS: %s seconds" % (time.time() - start_time_dfs))
  print_maze(maze_for_dfs)

  start_time_bfs = time.time()
  bfs_maze_solver(maze_for_bfs, [1, 1], [m-2, n-2])
  print("Execution time BFS: %s seconds" % (time.time() - start_time_bfs))
  print_maze(maze_for_bfs)

  start_time_dijkstra = time.time()
  dijkstra_maze_solver(maze_for_dijkstra, [1, 1], [m-2, n-2])
  print("Execution time Dijkstra: %s seconds" % (time.time() - start_time_dijkstra))
  print_maze(maze_for_dijkstra)

  start_time_a_estrella = time.time()
  astar_maze_solver(maze_for_astar, [1, 1], [m-2, n-2])
  print("Execution time A*: %s seconds" % (time.time() - start_time_a_estrella))
  print_maze(maze_for_astar)

if __name__ == "__main__":
  main()