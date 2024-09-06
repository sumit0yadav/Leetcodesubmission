from collections import deque
class Solution:
    def findOrder(self, n: int, prereq: List[List[int]]) -> List[int]:

        ind={}
        
        adj={}
        for i in range(n):
            adj[i]=[]
            ind[i]=0
        for course in prereq:
            x,y=course[0],course[1]
            adj[y].append(x)
            ind[x]+=1
        q=deque()
        for i in range(n):
            if ind[i]==0:
                q.append(i)
        ans=0
        res=[]
        while q:
            curr=q.popleft()
            ans+=1
            res.append(curr)

            for nei in adj[curr]:
                ind[nei]-=1
                if ind[nei]==0:
                    q.append(nei)
        if n!=ans:return []
        return res
        
        