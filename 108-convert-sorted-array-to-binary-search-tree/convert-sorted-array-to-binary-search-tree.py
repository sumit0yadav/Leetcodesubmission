# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def h(arr,start,end):
            if start>end:
                return None
            mid=(start+end)//2
            node=TreeNode(arr[mid])
            node.left=h(arr,start,mid-1)
            node.right=h(arr,mid+1,end)
            return node
        return h(nums,0,len(nums)-1)
            
        