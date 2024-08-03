# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict,deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:return []
        curr=root
        q= deque()
        nodes=[]
        q.append((curr,0,0))

        while q:
            node,x,y=q.popleft()
            nodes.append((x,y,node.val))
            if node.left:
                q.append((node.left,x-1,y+1))
            if node.right:
                q.append((node.right,x+1,y+1))
        nodes.sort()

        res=defaultdict(list)

        for x,y,val in nodes:
            res[x].append(val)
        return [res[x] for x in sorted(res)]


        