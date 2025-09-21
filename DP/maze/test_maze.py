import pytest
from maze import grid_paths
def test_grid_paths_normal():
  assert grid_paths(18, 6) == 26334

def test_grid_paths_large():
  assert grid_paths(75, 19) == 5873182941643167150