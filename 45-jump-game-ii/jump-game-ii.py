class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:return 0
        if nums[0]>=len(nums)-1:return 1
        currfar=0
        currend=0
        jump=0
        for i in range(len(nums)-1):
            currfar=max(currfar,i+nums[i])
            if i==currend:
                currend=currfar
                jump+=1
        return jump
        