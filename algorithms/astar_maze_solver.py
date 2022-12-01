import math
from utils.get_neighbours_for_astar import get_neighbours_for_astar
from utils.sort_dictionary import sort_dictionary

def astar_maze_solver(maze, start, end):
  """
  It takes a maze, a start and an end, and returns the path from start to end
  
  :param maze: the maze to be solved
  :param start: (1, 1)
  :param end: the end point of the maze
  """

  path = []
  visited = []
  queue = {}

  # Create a dictionary with the distance from start to each node
  # The distance from start to start is 0 and to all the others is infinite
  # Remember that the nodes are tuples (x, y) and they are the elements of the grid
  distance = {}
  for i in range(len(maze)):
    if i % 2 != 0:
      for j in range(len(maze)):
        if i == start[0] and j == start[1]:
          distance[(i, j)] = 0
        elif j % 2 != 0:
          distance[(i, j)] = math.inf

  heuristic = {}
  for i in range(len(maze)):
    if i % 2 != 0:
      for j in range(len(maze)):
        if j % 2 != 0:
          heuristic[(i, j)] = abs(end[0] - i) + abs(end[1] - j)
        
  prev_nodes = {}
  for i in range(len(maze)):
    if i % 2 != 0:
      for j in range(len(maze)):
        if i == start[0] and j == start[1]:
          prev_nodes[(i, j)] = None
        elif j % 2 != 0:
          prev_nodes[(i, j)] = None

  actual = start

  while actual[0] != end[0] or actual[1] != end[1]:

    visited.append(actual)

    current_weight = distance[tuple(actual)]

    neighbours = get_neighbours_for_astar(maze, actual[0], actual[1], visited, heuristic)
    coordinates_neighbours = list(neighbours.keys())

    for i in range(len(coordinates_neighbours)):
      if coordinates_neighbours[i] not in visited:
        queue[coordinates_neighbours[i]] = neighbours[coordinates_neighbours[i]]
    
    for i in range(len(queue)):
      queue[list(queue.keys())[i]] += current_weight

    queue = sort_dictionary(queue)

    for i in range(len(queue)):
      if distance[queue[i][0]] > current_weight + queue[i][1]:
        distance[queue[i][0]] = current_weight + queue[i][1]
        prev_nodes[queue[i][0]] = actual

    actual = queue[0][0]

    queue = dict(queue[1:])

  actual = end
  while actual != start:
    path.append(actual)
    actual = prev_nodes[tuple(actual)]

  path.append(start)

  for i in range(len(path)):
    if i < len(path)-1:
      actual = path[i]
      next = path[i+1]
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

    maze[path[i][0]][path[i][1]] = '2'