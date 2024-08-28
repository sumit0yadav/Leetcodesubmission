# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:return []
        q=deque()
        res=[]
        curr=root
        q.append(curr)
        
        while q:
            ans=[]
            size=len(q)
            for i in range(size):
                x=q.popleft()
                if x.left:q.append(x.left)
                if x.right:q.append(x.right)
                ans.append(x.val)
            res.append(ans)
        return res
            
