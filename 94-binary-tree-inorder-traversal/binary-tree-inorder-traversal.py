# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []
        curr=root
        res=[]

        while curr:
            if curr.left is None:
                res.append(curr.val)
                curr=curr.right
            else:
                prev=curr.left
                while prev.right and prev.right!=curr:
                    prev=prev.right
                if prev.right is None:
                    prev.right=curr
                    curr=curr.left
                elif prev.right==curr:
                    
                    res.append(curr.val)
                    curr=curr.right
                    prev.right=None
        return res
        