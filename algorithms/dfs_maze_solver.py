import random
from utils.get_neighbours_for_search import get_neighbours_for_search

def dfs_maze_solver(maze, start, end):
  """
  It takes a maze, a start and an end, and returns a solved maze
  
  :param maze: The maze to be solved
  :param start: The starting point of the maze
  :param end: The end point of the maze
  """
  
  visited = []
  stack = []
  neighbours = []
  
  actual = start
  
  while True:
    visited.append(actual)
  
    # Obtener neighbours
    neighbours = get_neighbours_for_search(maze, actual[0], actual[1], visited)

    if neighbours:
      neighbour = random.choice(neighbours)
      visited.append(neighbour)
      stack.append(actual)
      actual = neighbour
  
    else:
      if stack:
        actual = stack.pop()
      else:
        break
  
    if actual == end:
      break

  for i in range(len(visited)):
    if i < len(visited)-1:
      actual = visited[i]
      next = visited[i+1]
      # Obtener la coordenada entre visited[i] y visited[i+1]
      if actual[0] == next[0]:
        if actual[1] < next[1]:
          maze[actual[0]][actual[1]+1] = '2'
        elif actual[1] > next[1]:
          maze[actual[0]][actual[1]-1] = '2'
      elif actual[1] == next[1]:
        if actual[0] < next[0]:
          maze[actual[0]+1][actual[1]] = '2'
        elif actual[0] > next[0]:
          maze[actual[0]-1][actual[1]] = '2'

    maze[visited[i][0]][visited[i][1]] = '2'