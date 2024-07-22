class Solution:
    def rob(self, nums: List[int]) -> int:

        def h(nums,i,dp):
            if i>=len(nums):
                return 0
            if i in dp:
                return dp[i]
            take= nums[i]+h(nums,i+2,dp)
            nottake=h(nums,i+1,dp)
            dp[i]=max(take,nottake)
            return dp[i]
        dp={}
        return h(nums,0,dp)
        