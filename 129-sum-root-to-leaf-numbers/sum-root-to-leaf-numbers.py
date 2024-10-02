# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def h(node,curr):
            if node is None:return 0
            curr=curr*10+node.val
            
            
            
            left=h(node.left,curr)
            right=h(node.right,curr)
            if node.left and node.right:
                return left+right
            if node.left:
                return left
            if node.right:
                return right
            
            return curr
        return h(root,0)
        