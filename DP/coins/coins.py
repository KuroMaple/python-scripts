"""
coins.py

This module solves two classic dynamic programming problems:
1. **Minimum Coin Problem**: Find the minimum number of coins needed to make 
      a given target sum
2. **Coin Change Probelm**: Determine the number of distinct ways to make a 
      given target sum using a set of coin denominations

Functions:
- `min_coins`
- `min_ignore_none`
- `how_many_ways`

Author:
  Hassan Hashmi
""" 
from collections import defaultdict

def min_coins(coins: list[int], target_sum: int) -> int:
  """
  Compute the minimum number of coins needed to sum to target sum
  
  Parameters
  ----------
  coins : list[int]
          Coin denominations (positive integers)
  target_sum :  int
                The goal to sum to

  Returns
  -------
  int | None
    The smallest number of coins to make target_sum or None if not possible
    
  Notes
  -----
  - Uses bottom-up DP
  - O(target_sum * len(coins)) time complexity
  
  """
  memo = {}
  memo[0] = 0
  for i in range(1, target_sum + 1):
    for coin in coins:
      subproblem = i - coin
      
      if subproblem < 0:
        continue
      memo_i = memo.get(i)
      memo_subproblem = memo.get(subproblem)
      memo_subproblem = memo_subproblem + 1 if memo_subproblem is not None else None
      memo[i] = min_ignore_none(memo_i, memo_subproblem)
  return memo[target_sum]

def min_ignore_none(a, b):
  """
  Return the non-none value or minimum of non-none values
  
  Parameters
  ----------
  a : None or int
  b : None or int
  
  Returns
  -------
  int : The non-none value or the minimum between two non-none values
  
  Notes
  -----
  - Assumes one of a or b is non-none
  """
  if not a:
    return b
  if not b:
    return a
  return min(a, b)

def how_many_ways(coins: list[int], target_sum: int) -> int:
  """
  Compute the number of ways to make target sum given coins
  
  Parameters
  ----------
  coins : list[int]
          Coin denominations (positive integers)
  target_sum :  int
                The goal to sum to
  
  Returns
  -------
  int : None
    The number of ways to make target_sum from coins         
  """
  memo = defaultdict(int)
  memo[0] = 1
  
  for coin in coins:
    for i in range(1, target_sum + 1):
      memo[i] += memo[i - coin]
      
  return memo[target_sum]