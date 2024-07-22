class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = {}
        dp[0] = 0
        dp[1]=nums[0]
        for i in range(1, len(nums)):
            val = nums[i]
            dp[i + 1] = max(dp[i], val + dp[i - 1])
        return dp[len(nums)]
