class Solution:
    from collections import deque
    def shortestSubarray(self, l: List[int], k: int) -> int:
        q=deque()
        sum=0
        ans=1e9
        for i in range(len(l)):
            sum+=l[i]
            if sum>=k:ans=min(ans,i+1)
            
            while q and sum<=q[-1][0]:
                q.pop()
            while q and sum-q[0][0]>=k:
                x=q.popleft()
                ans=min(ans,i-x[1])

            q.append([sum,i])
        if ans==1e9:return -1
        return ans



        