import heapq
class Solution:

    def minCostConnectPoints(self, p: List[List[int]]) -> int:

        def manh(p1,p2):
            return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
        n=len(p)
        adj=[[]*n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):  # Only compute for i < j to avoid duplicates
                dist = manh(p[i], p[j])
                adj[i].append((j, dist))
                adj[j].append((i, dist))

        hp=[(0,0)]
        # print(0,p[0])
        heapq.heapify(hp)
        vis=set()
        ans=0
        while len(vis)<n:
            wt,node=heapq.heappop(hp)
            if node in vis:
                continue
            vis.add(node)
            # print(ans,wt,node)
            ans+=wt
            for nei,wt in adj[node]:
                if nei not in vis:
                    heapq.heappush(hp,(wt,nei))
        return ans
                    
        