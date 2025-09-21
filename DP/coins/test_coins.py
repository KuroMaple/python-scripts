import pytest
from coins import min_coins

def test_small_sum():
  assert min_coins([1, 4, 5], 13) == 3

def test_large_sum():
  assert min_coins([1, 4, 5], 150) == 30
  
