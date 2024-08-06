# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def h(curr,cnt,k,ans):
            if not curr:return
            
            h(curr.left,cnt,k,ans)
            cnt[0]+=1
            if cnt[0]==k:
                ans[0]=curr.val
                return
            h(curr.right,cnt,k,ans)
        cnt=[0]
        ans=[-1000]
        h(root,cnt,k,ans)
        return ans[0]
            
        