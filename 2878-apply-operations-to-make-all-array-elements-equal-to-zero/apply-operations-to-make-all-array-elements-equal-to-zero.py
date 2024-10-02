from typing import List

class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:

        n = len(nums)
        if k == 1:
            return True
        
        delta = [0] * (n + 1)  # To store the cumulative effect of subtractions
        
        curr_effect = 0  # To track the current cumulative effect
        for i in range(n):
            curr_effect += delta[i]  # Apply the effect to the current element
            nums[i] -= curr_effect    # Apply the accumulated effect to the current number
            
            if nums[i] < 0:  # If we go negative, the array can't be valid
                return False
            
            if nums[i] > 0:  # If nums[i] > 0, we need to reduce it in the next k elements
                if i + k > n:  # If there aren't enough elements left for a full k-length window
                    return False
                
                # Record the effect of subtracting nums[i] from the next k elements
                curr_effect += nums[i]
                delta[i + k] -= nums[i]  # Remove the effect after k steps
                nums[i] = 0  # After applying the subtraction, nums[i] becomes 0
        
        return all(num == 0 for num in nums)
