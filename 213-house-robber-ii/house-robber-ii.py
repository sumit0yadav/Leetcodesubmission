class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:return 0
        if len(nums)==1:return nums[0]
        if len(nums)==2:return max(nums)
        def h(nums,dp,i):
            if i>=len(nums):
                return 0
            if i in dp:
                return dp[i]
            take=nums[i]+h(nums,dp,i+2)
            nottake=h(nums,dp,i+1)
            dp[i]=max(take,nottake)
            return dp[i]
        
        dp1,dp2={},{}
        a1=nums[1:]
        a2=nums[:-1]
        return max(h(a1,dp1,0),h(a2,dp2,0))