class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        for  i in range(2**n):
            res=[]
            for j in range(n):
                if 1<<j & i:
                    res.append(nums[j])
            ans.append(res)
        return ans
        