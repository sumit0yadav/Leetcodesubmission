class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp={}
        @cache
        def h(i,mustpick):
            if i>=len(nums):
                if mustpick:return 0
                return -1e9
            # if (i,mustpick) in dp:return dp[(i,mustpick)]
            if mustpick:
                return max(0,h(i+1,True)+nums[i])
            else:
                return max(h(i+1,False),nums[i]+h(i+1,True))
        return h(0,False)

        