# class Solution:
#     def isBipartite(self, graph: List[List[int]]) -> bool:

#         def h(adj,vis,node):
#             q=deque()
#             q.append(node)
#             vis[node]=0

#             while q:
#                 node = q.popleft()

#                 for nei in adj[node]:
#                     if nei not in vis:
#                         vis[nei]=1-vis[node]
#                     elif(vis[nei]==vis[node]):return False
#             return True
#         vis={}
#         for i in range(len(graph)):
#             if i not in vis:
#                 if(h(graph,vis,i)==False):return False
#         return True   
from typing import List
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        def h(adj, vis, node):
            q = deque()
            q.append(node)
            vis[node] = 0  # Start coloring the node with color 0

            while q:
                node = q.popleft()

                for nei in adj[node]:
                    if nei not in vis:
                        vis[nei] = 1 - vis[node]  # Alternate color
                        q.append(nei)
                    elif vis[nei] == vis[node]:
                        return False
            return True

        vis = {}
        for i in range(len(graph)):
            if i not in vis:
                if not h(graph, vis, i):  # Pass the correct starting node i
                    return False
        return True
