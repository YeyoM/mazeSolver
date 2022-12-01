import random
from utils.get_neighbours import get_neighbours

def carve(maze):
  
  visited = []
  stack = []
  neighbours = []
  actual = [1, 1]

  while True:

    visited.append(actual)

    neighbours = get_neighbours(maze, actual[0], actual[1], visited)

    if neighbours:
      neighbour = random.choice(neighbours)
      visited.append(neighbour)
      stack.append(actual)

      maze[int((actual[0]+neighbour[0])/2)][int((actual[1]+neighbour[1])/2)] = '1'

      actual = neighbour

    else:
      if stack:
        actual = stack.pop()
      else:
        break