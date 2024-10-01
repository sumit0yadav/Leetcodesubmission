# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:

        def h(node):
            if not node.left and not node.right:
                # print(True,node.val,node.val,node.val)
                return True,node.val,node.val,node.val,node.val

            if node.left:
                isbst_left,min_left,max_left,sum_left,maxsum_left=h(node.left)
            else:
                isbst_left,min_left,max_left,sum_left,maxsum_left=True,1e9,-1e9,0,0

            if node.right:
                isbst_right,min_right,max_right,sum_right,maxsum_right=h(node.right)
            else:
                isbst_right,min_right,max_right,sum_right,maxsum_right=True,1e9,-1e9,0,0

            isbst= isbst_left and isbst_right and (max_left<node.val<min_right)
            if isbst:
                # if node.val==2:
                #     print(min_right,'val',node.right.val)
                #     print(True,node.val,min_left,max_right,sum_left,sum_right,sum_left+sum_right+node.val)
                x=max(sum_left+sum_right+node.val,maxsum_left,maxsum_right)
                print('True',node.val,x)
                
                return True,min(node.val,min_left),max(max_right,node.val),sum_left+sum_right+node.val,x
            else:
                y=max(maxsum_left,maxsum_right)
                print('False',node.val,y)
                
                return False,1e9,-1e9,max(sum_left,sum_right),y

        a,b,c,d,e= h(root)
        # print(a,d,e)
        return max(0,e)
            
        