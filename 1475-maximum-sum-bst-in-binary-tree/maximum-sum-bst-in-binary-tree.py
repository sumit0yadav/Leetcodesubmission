from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def postOrderTraverse(node: Optional[TreeNode]):
            if node is None:
                return [float('inf'), float('-inf'), 0]  # [min, max, sum], initialize min=inf, max=-inf

            left = postOrderTraverse(node.left)
            right = postOrderTraverse(node.right)

            # The BST is valid if the left subtree is valid, the right subtree is valid,
            # the current node's value is greater than the max value of the left subtree,
            # and less than the min value of the right subtree.
            if not (left and right and node.val > left[1] and node.val < right[0]):
                return None

            # Calculate the sum of the current BST.
            sumBST = node.val + left[2] + right[2]
            nonlocal maxSum
            maxSum = max(maxSum, sumBST)
            
            # Calculate the new min and max for the current subtree.
            minVal = min(node.val, left[0])
            maxVal = max(node.val, right[1])
            
            return [minVal, maxVal, sumBST]

        maxSum = 0
        postOrderTraverse(root)
        return maxSum

# Example Usage
# if __name__ == "__main__":
#     # Construct a binary tree
#     root = TreeNode(1)
#     root.left = TreeNode(4)
#     root.right = TreeNode(3)
#     root.left.left = TreeNode(2)
#     root.left.right = TreeNode(4)
#     root.right.left = TreeNode(2)
#     root.right.right = TreeNode(5)
#     root.right.right.left = TreeNode(4)
#     root.right.right.right = TreeNode(6)
