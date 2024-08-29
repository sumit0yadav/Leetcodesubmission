# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        curr=root
        self.maxsum=0
        def h(curr):
            if not curr:
                return True,0,1e9,-1e9
            l,lsum,lmin,lmax=h(curr.left)
            r,rsum,rmin,rmax=h(curr.right)

            if l and r and(lmax<curr.val<rmin):
                self.maxsum=max(self.maxsum,curr.val+lsum+rsum)
                return True,curr.val+lsum+rsum,min(lmin,curr.val),max(rmax,curr.val)
            else:
                self.maxsum=max(self.maxsum,lsum,rsum)

                return False, max(lsum,rsum),1e9,-1e9
        x=h(root)
        return self.maxsum
        