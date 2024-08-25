class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    
        cnt=0
        for i in range(len(nums)):
            if cnt==0:
                ele=nums[i]
                

            k=nums[i]
            if k==ele:
                cnt+=1
            else:
                cnt-=1
        cnt=0
        for i in range(len(nums)):
            if nums[i]==ele:
                cnt+=1
        if cnt>len(nums)//2:
            return ele
        else:
            return -1

            


