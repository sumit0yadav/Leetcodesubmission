from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n=len(nums)

        q=deque()
        sum=0
        res=1e9
        ans=1e9

        for i in range(n):
            sum+=nums[i]
            if sum>=k:
                ans=min(ans,i+1)
            while q and sum-q[0][0]>=k:
                x=q.popleft()
                ans=min(ans,i-x[1])
            while q and q[-1][0]>=sum:
                q.pop()
            q.append([sum,i])

        if ans==1e9:return -1
        return ans


        