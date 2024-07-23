class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        def h(adj,vis,node):
            q=deque()
            q.append(node)
            vis[node]=0

            while q:
                node = q.popleft()

                for nei in adj[node]:
                    if nei not in vis:
                        vis[nei]=1-vis[node]
                        q.append(nei)
                    elif(vis[nei]==vis[node]):return False
            return True
        vis={}
        for i in range(len(graph)):
            if i not in vis:
                if(h(graph,vis,i)==False):return False
        return True   