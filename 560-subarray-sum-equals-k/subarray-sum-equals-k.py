class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt=0
        hm={}

        hm[0]=1
        summ=0
        for i in range(len(nums)):
            summ+=nums[i]
            pre=summ-k
            if pre in hm:
                cnt+=hm[pre]
            if summ in hm:
                hm[summ]+=1
            else:
                hm[summ]=1
        return cnt
            