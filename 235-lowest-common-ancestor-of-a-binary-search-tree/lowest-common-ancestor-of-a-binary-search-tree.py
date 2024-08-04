# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def h(curr,p,q):
            if curr==None or curr==p or curr==q:
                return curr
            left=h(curr.left,p,q)
            right=h(curr.right,p,q)
            if left is None:return right
            elif right is None:return left
            else:return curr
        
        curr=root
        return h(curr,p,q)
        