# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inhm={}
        prehm={}
        for i in range(len(preorder)):
            prehm[preorder[i]]=i
            inhm[inorder[i]]=i


        def h(pre,ino,prestart,preend,instart,inend,inhm):
            if prestart>preend or instart>inend:
                return None

            node=TreeNode(pre[prestart])
            inroot=inhm[node.val]
            size=inroot-instart
            node.left=h(pre,ino,prestart+1,prestart+size,instart,inroot,inhm)
            node.right=h(pre,ino,prestart+size+1,preend,inroot+1,inend,inhm)
            return node
        return h(preorder,inorder,0,len(preorder)-1,0,len(inorder)-1,inhm)

           