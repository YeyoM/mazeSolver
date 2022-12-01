from utils.get_neighbours_for_search import get_neighbours_for_search

def get_neighbours_for_dijkstra(maze, i, j, visited):
  """
  It returns a dictionary of all the neighbours of the current cell, with the weight of the edge
  between the current cell and the neighbour being 2
  
  :param maze: The maze we're searching
  :param i: the row index of the current cell
  :param j: the column of the current cell
  :param visited: a list of tuples of the form (i, j) that represent the coordinates of the cells that
  have already been visited
  :return: A dictionary of tuples of the neighbours and their weights.
  """

  neighbours = get_neighbours_for_search(maze, i, j, visited)
  
  weighted_neighbours = {}

  for neighbour in neighbours:
    weighted_neighbours[tuple(neighbour)] = 2
  
  return weighted_neighbours