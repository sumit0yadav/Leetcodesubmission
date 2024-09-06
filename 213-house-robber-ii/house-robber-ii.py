from functools import lru_cache
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)
        
        # Define the helper function with lru_cache for memoization
        @lru_cache(None)
        def h(i, nums):
            if i >= len(nums):
                return 0
            take = nums[i] + h(i + 2, nums)
            nottake = h(i + 1, nums)
            return max(take, nottake)
        
        # Exclude the first house or the last house and calculate the maximum
        return max(h(0, tuple(nums[1:])), h(0, tuple(nums[:-1])))

