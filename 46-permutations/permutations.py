class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def back(ind,res):
            if len(res)==len(nums):
                ans.append(list(res))
                return
            for ele in nums:
                if ele not in res:
                    res.append(ele)
                    back(ind+1,res)
                    res.pop()
        back(0,[])
        return ans
