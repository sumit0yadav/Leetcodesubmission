from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def h(nums, dp, i, sum):
            if sum == 0:
                return 0  # No coins needed
            if sum < 0 or i == len(nums):
                return float('inf')  # Invalid path
            
            # Check if the result for this state is already computed
            if (i, sum) in dp:
                return dp[(i, sum)]
            
            # Include the current coin
            take = 1 + h(nums, dp, i, sum - nums[i])
            # Exclude the current coin
            nottake = h(nums, dp, i + 1, sum)
            
            # Store the result in dp dictionary and return
            dp[(i, sum)] = min(take, nottake)
            return dp[(i, sum)]

        dp = {}
        result = h(coins, dp, 0, amount)
        return result if result != float('inf') else -1  # Return -1 if no solution
