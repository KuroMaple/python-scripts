"""
fibonacci.py

This module provide a function to compute the n-th Fibonacci number 
using dymanic programming in O(n) time.

Author: Hassan Hashmi
"""
from typing import Dict


def fib(n: int) -> int:
  """
  Compute the n-th fibonacci number
  
  Parameters:
  ----------
  n : int 
      The position (1-based) in the Fibonacci Sequence.
  
  Returns:
  ----------
  int
    The n-th Fibonacci number.
  
  Notes:
  ----------
  - The Fibonacci sequence is defined as

  
  """
  memo = {}
  for i in range(1, n + 1):
    result = -1 # initilized result, even though in python scoping is different and res can 
    if i <= 2:
      result = 1
    else:
      result = memo[i - 1] + memo[i - 2]
    memo[i] = result
  return memo[n]
      

if __name__ == '__main__':
  print("Please enter the n value for our fibonacci sequence: ")
  n = int(input().strip())
  ans = fib(n)
  print(f'ANSWER: {str(ans)} \n')