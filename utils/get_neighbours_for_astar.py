from utils.get_neighbours_for_search import get_neighbours_for_search

def get_neighbours_for_astar(maze, i, j, visited, heuristic):
  """
  It returns a dictionary of neighbours of the current cell, with the keys being the coordinates of
  the neighbours and the values being the weights of the neighbours
  
  :param maze: The maze we're searching
  :param i: the row index of the current cell
  :param j: the column of the current cell
  :param visited: a list of tuples of the form (i, j) that represent the coordinates of the cells that
  have already been visited
  :param heuristic: a dictionary of tuples (i, j) to the heuristic value of that cell
  :return: A dictionary of the neighbours of the current node, with the key being the neighbour and
  the value being the weight of the edge between the current node and the neighbour.
  """

  neighbours = get_neighbours_for_search(maze, i, j, visited)
  
  weighted_neighbours = {}

  for neighbour in neighbours:
    weighted_neighbours[tuple(neighbour)] = 2 + heuristic[tuple(neighbour)]
  
  return weighted_neighbours