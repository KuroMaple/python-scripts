import pytest
from coins import min_coins, how_many_ways

def test_min_coins_small_sum():
  assert min_coins([1, 4, 5], 13) == 3

def test_min_coins_large_sum():
  assert min_coins([1, 4, 5], 150) == 30

def test_how_many_ways_simple():
  assert how_many_ways([1, 4, 5], 5) == 3
  '''
  1 4 
  1 1 1 1 1
  5
  '''
  
def test_how_many_ways_medium():
  assert how_many_ways([1, 2, 3], 4) == 4
  
def test_how_many_ways_edge():
  assert how_many_ways([1, 2, 5], 0) == 1
