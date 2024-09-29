from typing import List
from bisect import bisect_left

class Solution:
    def jobScheduling(self, st: List[int], et: List[int], profit: List[int]) -> int:
        # Combine start times, end times, and profits into a single list of tuples
        emp = sorted(zip(st, et, profit))  # Sort by end time
        
        # Extract start times and end times for binary search
        start_times = [job[0] for job in emp]
        
        # Memoization dictionary to store the result of subproblems
        dp = {}
        
        # Helper function to maximize profit
        def h(ind: int) -> int:
            # Base case: no jobs left to schedule
            if ind == len(emp):
                return 0
            
            # Check if the result is already computed
            if ind in dp:
                return dp[ind]
            
            # Option 1: Skip the current job
            not_take = h(ind + 1)
            
            # Option 2: Take the current job
            curr_start, curr_end, curr_profit = emp[ind]
            # Use binary search to find the next non-conflicting job
            next_job = bisect_left(start_times, curr_end)
            take = curr_profit + h(next_job)
            
            # Memoize the result
            dp[ind] = max(take, not_take)
            return dp[ind]
        
        # Start recursion from the first job
        return h(0)
