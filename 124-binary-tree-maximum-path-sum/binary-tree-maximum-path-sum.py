# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def h(node,maxval):
            if node is None:return 0

            left=h(node.left,maxval)
            right=h(node.right,maxval)

            maxval[0]=max(maxval[0],left+right+node.val)
            return max(0,max(left,right)+node.val)
        
        maxval=[-1e9]
        h(root,maxval)
        return maxval[0]

        