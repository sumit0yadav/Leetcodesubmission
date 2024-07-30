from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def reverse(adj):
  
            reversed_adj = [[] for _ in range(len(adj))]
            
            for u in range(len(adj)):
                for v in adj[u]:
                    reversed_adj[v].append(u)
                    
            return reversed_adj
        
        adj=reverse(graph)
        ind=[0]*len(adj)
        for i in range(len(adj)):
            for ele in adj[i]:
                ind[ele]+=1
        q=deque()
        for i in range(len(ind)):
            if ind[i]==0:
                q.append(i)
        
        st=set()
        vert=set(range(len(adj)+1))
        while q:

            node = q.popleft()
            st.add(node)
            for nei in adj[node]:
                ind[nei]-=1
                if ind[nei]==0:
                    q.append(nei)
        ans=list(st)
        ans.sort()
        return ans
            
        

        
        