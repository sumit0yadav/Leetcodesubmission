class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        ans=0
        

        i=0
        while i<len(nums):
            cnt=0
            while i<len(nums) and nums[i]==1:
                cnt+=1
                i+=1
            else:
                i+=1

            ans=max(cnt,ans)
            
        return ans


        