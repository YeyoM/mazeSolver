import numpy as np

def generate_grid(n, m, maze):
  """
  This function creates a grid of size m x n, 
  where m and n are odd numbers, and fills it with 0s and 1s. 
  
  The function returns a matrix of size m x n. 
  
  :param n: number of columns
  :param m: number of rows
  :param maze: the maze to be generated
  :return: A 2D array of size m x n 
  """

  maze = np.full((m, n), '0')
  
  for i in range(m):
    if i % 2 == 0:
      maze[i] = np.full(n, '0')
    else:
      for j in range(n):
        if j % 2 == 0:
          maze[i][j] = '0'
        else:
          maze[i][j] = '1'

  return maze