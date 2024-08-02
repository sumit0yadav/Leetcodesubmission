# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        curr=root
        res=[]
        def ino(curr,res):
            if curr is None:
                return
            ino(curr.left,res)
            res.append(curr.val)
            ino(curr.right,res)
        ino(curr,res)
        return res

        