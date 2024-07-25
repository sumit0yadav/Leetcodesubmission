class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:return True
        reach=0
        for i in range(len(nums)):
            
            if i>reach:return False
            if i==len(nums)-1:return True

            reach=max(reach,nums[i]+i)
        return True