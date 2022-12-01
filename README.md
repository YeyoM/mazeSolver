<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/YeyoM/mazeSolver">
    <img src="public/icon.svg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Maze Solver</h3>

  <p align="center">
    Generate and solve a maze with Python.
    <br />
    <a href="https://github.com/YeyoM/mazeSolver"><strong>Explore the code »</strong></a>
    <br />
    <br />
    <a href="https://github.com/YeyoM/mazeSolver/issues">Report Bug</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/YeyoM/mazeSolver)

### What does this project do?

This project uses various techniques to generate and solve a maze using python in an easy way, to generate the maze we follow the following steps:

- Generate a matrix full of 0's which represents obtacles
- Generate a grid in the matrix with 1's which representes paths that the algorithm will be able to follow
- Using DFS we "carve" the maze generating paths between spaces in the grid which, seen from a graph approach, the spaces in the grid are nodes, the objective is to connect this nodes.

For the solution part, there are available 4 algorithms

#### DFS and BFS

BFS, Breadth-First Search, is a vertex-based technique for finding the shortest path in the graph. It uses a Queue data structure that follows first in first out. In BFS, one vertex is selected at a time when it is visited and marked then its adjacent are visited and stored in the queue. It is slower than DFS. 

DFS, Depth First Search, is an edge-based technique. It uses the Stack data structure and performs two stages, first visited vertices are pushed into the stack, and second if there are no vertices then visited vertices are popped. 

#### Dijkstra

Dijkstra's algorithm allows us to find the shortest path between any two vertices of a graph. Djikstra used this property in the opposite direction i.e we overestimate the distance of each vertex from the starting vertex. Then we visit each node and its neighbors to find the shortest subpath to those neighbors.

The algorithm uses a greedy approach in the sense that we find the next best solution hoping that the end result is the best solution for the whole problem.

#### A* Star

Informally speaking, A* Search algorithms, unlike other traversal techniques, it has “brains” (in the code is called heuristic). What it means is that it is really a smart algorithm which separates it from the other conventional algorithms. This fact is cleared in detail in below sections. 
And it is also worth mentioning that many games and web-based maps use this algorithm to find the shortest path very efficiently (approximation). 

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

- Have python installed in your computer

- Install with pip the following: random, numpy and time.

- Clone the repo
   ```sh
    git clone https://github.com/YeyoM/mazeSolver.git
   ```
- The entry point of the code is main.py

<!-- LICENSE -->
## License

Distributed under the MIT License. See LICENSE.txt for more information.

<!-- CONTACT -->
## Contact

YeyoM - [@YeyoMoreno24](https://twitter.com/YeyoMoreno24) - yeyomoreno2003@hotmail.com

Maze Solver - [https://github.com/YeyoM/mazeSolver](https://github.com/YeyoM/mazeSolver)

<!-- MARKDOWN LINKS & IMAGES -->
[product-screenshot]: public/screenshot.png