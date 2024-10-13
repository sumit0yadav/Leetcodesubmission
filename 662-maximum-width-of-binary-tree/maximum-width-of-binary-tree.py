# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        q=deque()
        q.append((root,0))

        res=1
        while q:
            
            first,last=q[0][1],q[-1][1]
            res=max(res,last-first+1)

            size=len(q)
            for _ in range(size):
                node,curr=q.popleft()
                if node.left:
                    q.append((node.left,2*curr+1))
                if node.right:
                    q.append((node.right,2*curr+2))
        return res
        