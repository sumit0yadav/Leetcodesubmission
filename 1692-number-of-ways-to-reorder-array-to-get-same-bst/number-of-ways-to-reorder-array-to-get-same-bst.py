class Solution:
    import math

    def numOfWays(self, nums: List[int]) -> int:
        mod=int(1e9+7)

        def h(nums):
            if len(nums)<3:return 1
            # if len(nums)==3:
                # y=
            root=nums[0]
            left=[x for x in nums[1:] if root>x]
            right=[x for x in nums[1:] if root<x]
            l=h(left)%mod
            r=h(right)%mod
            pro=(l*r)%mod
            return (pro*math.comb(len(nums)-1,len(left)))%mod
        return h(nums)-1
            
        