
from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        k-=1
        adj=[[]for _ in range(n)]
        for time in times:
            adj[time[0]-1].append((time[1]-1,time[2]))
        q=deque()
        q.append((k,0))
        dist=[float('inf')]*n
        dist[k]=0

        while q:

            node,cost=q.popleft()

            for adjnode,wei in adj[node]:
                if wei+cost<dist[adjnode]:
                    dist[adjnode]=cost+wei
                    q.append((adjnode,cost+wei))
        maxtime=max(dist)
        if maxtime==float('inf'):return -1
        return maxtime


        

        