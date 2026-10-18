import math
from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        def dfs(arr: List[int]) -> int:
            if len(arr) <= 2:
                return 1
                
            root = arr[0]
            
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            
            combinations = math.comb(len(left) + len(right), len(left))
            
            return combinations * dfs(left) * dfs(right)
            
        return (dfs(nums) - 1) % MOD