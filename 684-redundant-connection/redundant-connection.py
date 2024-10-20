class Solution:
    from collections import defaultdict
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def already(x,y,adjj,viss):
            if x==y:return True

            for x_ in adjj[x]:
                if x_ not in vis:
                    vis.add(x_)
                    if already(x_,y,adjj,viss):
                        return True
            return False
        adj=defaultdict(list)
        for edge in edges:
            vis=set()
            x,y=edge[0],edge[1]
            if already(x,y,adj,vis):
                return edge
            adj[x].append(y)
            adj[y].append(x)
        
        