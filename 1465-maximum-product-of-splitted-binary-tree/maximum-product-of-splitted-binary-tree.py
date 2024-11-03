# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
    
        total=0
        ans=[0]
        ans[0]=0
        def s(node):
            if node is None:return 0
            curr=node.val+s(node.left)+s(node.right)
            ans[0]=max(ans[0],curr*(total-curr))
            return curr
        # ans=0
        total=s(root)
        s(root)
        mod=1e9+7
        return int(ans[0]%mod)



        