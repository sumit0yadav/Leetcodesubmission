# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        # Global variable to track the maximum sum of any valid BST
        self.max_sum = 0
        
        def h(curr):
            if not curr:
                return True, 0, float('inf'), float('-inf')
            
            l, lsum, lmin, lmax = h(curr.left)
            r, rsum, rmin, rmax = h(curr.right)
            
            # Check if the current tree rooted at `curr` is a valid BST
            if l and r and lmax < curr.val < rmin:
                # Sum of the current BST
                curr_sum = curr.val + lsum + rsum
                # Update the global maximum sum if the current BST sum is larger
                self.max_sum = max(self.max_sum, curr_sum)
                # Return valid BST info
                return True, curr_sum, min(lmin, curr.val), max(rmax, curr.val)
            else:
                # If it's not a valid BST, return False and just keep the larger subtree sum
                return False, max(lsum, rsum), float('-inf'), float('inf')
        
        # Call the helper function and start the process
        h(root)
        
        # Return the maximum sum of any valid BST found in the tree
        return self.max_sum
