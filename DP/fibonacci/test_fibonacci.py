import pytest
from fibonacci import fib

def test_small_numbers():
  assert fib(1) == 1
  assert fib(2) == 1
  assert fib(3) == 2
  assert fib(4) == 3
  assert fib(5) == 5

def test_larger_numbers():
  assert fib(10) == 55
  assert fib(20) == 6765
  assert fib(50) == 12586269025

def test_invalid_input():
  with pytest.raises(ValueError):
    fib(-1)
  with pytest.raises(ValueError):
    fib(0)
