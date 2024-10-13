from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        size=len(graph)
        colors=[0]*size
        for i in range(size):
            if colors[i]!=0:continue
            q=deque()
            q.append(i)
            colors[i]=1
            while q:
                curr=q.popleft()
                for next in graph[curr]:
                    if colors[next]==0:
                        colors[next]=-colors[curr]
                        q.append(next)
                    elif colors[next]==colors[curr]:
                        return False
        return True

        