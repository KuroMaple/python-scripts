"""
fibonacci.py

This module provides a function to compute the n-th Fibonacci number 
using dynamic programming in O(n) time.

Author: 
  Hassan Hashmi
"""
from typing import Dict


def fib(n: int) -> int:
  """
  Compute the n-th Fibonacci number.
  
  Parameters
  ----------
  n : int
      The position (1-based) in the Fibonacci sequence.
  
  Returns
  -------
  int
      The n-th Fibonacci number.
  
  Notes
  -----
  - The Fibonacci sequence is defined as:
    F(1) = 1, F(2) = 1, F(n) = F(n-1) + F(n-2) for n > 2
  - This implementation uses a dictionary to store intermediate results.
  - Time complexity: O(n)
  - Space complexity: O(n)
  """
  if n <= 0:
    raise ValueError("n must be a positive integer.")
  
  memo: Dict[int, int] = {}
  for i in range(1, n + 1):
    if i <= 2:
      memo[i] = 1
    else:
      memo[i] = memo[i - 1] + memo[i - 2]
      
  return memo[n]
      
# -------------------------------
# CLI Entry Point
# -------------------------------
if __name__ == '__main__':
  try:
    n = int(input("Enter the position n for the Fibonacci sequence: ").strip())
    print(f"The {n}-th Fibonacci number is: {fib(n)}")
  except ValueError as ve:
    print(f"Error: {ve}")