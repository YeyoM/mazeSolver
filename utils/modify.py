import random

def modify(maze, m, n):
  for i in range(35):
    x = random.randint(1, n-2)
    y = random.randint(1, m-2)
    maze[x][y] = '1'