class Solution:
    from collections import deque
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=[[] for _ in range(n)]
        for ele in flights:
            adj[ele[0]].append([ele[1],ele[2]])
        q=deque()
        q.append((0,src,0))
        dist=[1e9]*n
        dist[src]=0

        while q:
            stops,node,cost=q.popleft()
            if stops>k:continue
            for nei,neicost in adj[node]:
                if cost+neicost<dist[nei]:
                    dist[nei]=cost+neicost
                    q.append((stops+1,nei,cost+neicost))
        if dist[dst]==1e9:return -1
        return dist[dst]




        