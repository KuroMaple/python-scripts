"""
coins.py

This module solves the DP minimum coin problem

Author:
  Hassan Hashmi
""" 

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
  int : None
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
  if not a:
    return b
  if not b:
    return a
  return min(a, b)

