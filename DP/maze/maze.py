"""
maze.py

This module solves the below probelem

Given an N x M grid, in how many ways can a rabbit get from the top-left to the 
  bottom-right corner if it can only move left or down?

Function:
- `grid_paths`

Author:
  Hassan Hashmi
"""
from typing import Dict
def grid_paths(n: int, m: int) -> int:
  """
  Compute the number of paths to reach the bottom left of a n x m grid
  
  Parameters
  ----------
  n : int
      Length of grid
  m : int 
      Height of grid
  
  Returns
  -------
  int : Number of paths possible to reach bottom left of grid
  """
  memo: Dict[tuple[int, int], int] = {} # n x m size of grid => number of paths to bottom left
  
  for i in range(1, n + 1):
    for j in range(1, m + 1):
      if i == 1 or j == 1:
        memo[(i, j)] = 1
      else:
        memo[(i, j)] = memo[(i - 1, j)] + memo[(i, j - 1)]
  return memo[(n, m)]