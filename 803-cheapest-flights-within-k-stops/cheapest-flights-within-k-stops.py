from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj=[[] for _ in range(n)]
        for flight in flights:
            adj[flight[0]].append((flight[1],flight[2]))
        q= deque([(0,src,0)])
        dist=[float('inf')]*n
        dist[src]=0
        while q:
            stops,node,cost=q.popleft()
            if stops>k:
                continue
            
            for adjnode,edw in adj[node]:
                if cost+edw<dist[adjnode]:
                    dist[adjnode]=cost+edw
                    q.append((stops+1,adjnode,edw+cost))
        return -1 if dist[dst]==float('inf') else dist[dst]        