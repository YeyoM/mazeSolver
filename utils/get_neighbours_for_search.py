from utils.get_neighbours import get_neighbours

def get_neighbours_for_search(maze, i, j, visited):
  """
  It returns the neighbours of a given cell in the maze, 
  but only if the cell is not a wall
  
  :param maze: The maze we're working with
  :param i: the current row
  :param j: column
  :param visited: a list of tuples that represent the coordinates of the cells that have been visited
  :return: A list of tuples.
  """

  partial_neighbours = get_neighbours(maze, i, j, visited)
  neighbours = []

  for neighbour in partial_neighbours:
    if neighbour[0] == i and neighbour[1] == j + 2 :
      if maze[i][j+1] == '1':
        neighbours.append(neighbour)
    elif neighbour[0] == i and neighbour[1] == j - 2:
      if maze[i][j-1] == '1':
        neighbours.append(neighbour)
    elif neighbour[0] == i + 2 and neighbour[1] == j:
      if maze[i+1][j] == '1':
        neighbours.append(neighbour)
    elif neighbour[0] == i - 2 and neighbour[1] == j:
      if maze[i-1][j] == '1':
        neighbours.append(neighbour)

  return neighbours