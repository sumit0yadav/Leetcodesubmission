
from collections import deque
class Solution:
    def calcEquation(self, equ: List[List[str]], val: List[float], que: List[List[str]]) -> List[float]:
        graph={}
        def build(eq,valu):
            
            for i in range(len(eq)):
                f,t=eq[i]
                v=valu[i]
                if f in graph:
                    graph[f].append((t,v))
                else:
                    graph[f]=[(t,v)]
            for i in range(len(eq)):
                f,t=eq[i]
                v=valu[i]
                if t in graph:
                    graph[t].append((f,1/v))
                else:
                    graph[t]=[(f,1/v)]
        def solve(query):
            f,t=query
            if f not in graph or t not in graph:
                return -1.0
            if f==t:return 1.0
            q=deque()
            q.append((f,1.0))
            vis=set()
            while q:
                curr,currval=q.popleft()
                vis.add(curr)
                if curr==t:
                    return currval
                for nei,val in graph[curr]:
                    if nei not in vis:
                        q.append((nei,currval*val))
            return -1.0
        build(equ,val)
        return [solve(q) for q in que]



        