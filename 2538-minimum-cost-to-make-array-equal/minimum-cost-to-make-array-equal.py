class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        arr=sorted(zip(nums,cost))
        total,cnt=sum(cost),0
        for num,c in arr:
            cnt+=c
            if total//2<cnt:
                target=num
                break
        res=0
        for num,c in arr:
            res+=abs(num-target)*c
        return res
        