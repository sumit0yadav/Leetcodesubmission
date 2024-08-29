# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        st=set()
        curr=root
        def ino(curr,k):
            if curr is None:
                return False
            if k-curr.val in st:
                return True
            st.add(curr.val)
            return ino(curr.left,k) or ino(curr.right,k)
        return ino(curr,k)
            
            
        