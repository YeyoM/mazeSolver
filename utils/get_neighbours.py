def get_neighbours(maze, i, j, visited):
  """
  It returns a list of all the neighbours of a given cell that haven't been visited yet
  
  :param maze: The maze we're trying to solve
  :param i: the current row
  :param j: the column of the current cell
  :param visited: a list of all the cells that have been visited
  :return: A list of neighbours that have not been visited.
  """

  neighbours = []

  if i > 1 and [i-2, j] not in visited:
    neighbours.append([i-2, j])
  
  if i < len(maze)-2 and [i+2, j] not in visited:
    neighbours.append([i+2, j])

  if j > 1 and [i, j-2] not in visited:
    neighbours.append([i, j-2])

  if j < len(maze[0])-2 and [i, j+2] not in visited:
    neighbours.append([i, j+2])

  return neighbours