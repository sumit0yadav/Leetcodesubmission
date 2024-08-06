# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

    
        if not root:return ''
        l=[]
        node=root
        q=deque()
        q.append(node)

        while q:
            
            curr=q.popleft()
            if curr:
                l.append(str(curr.val))
                q.append(curr.left)
                q.append(curr.right)
            else:
                l.append('#')
        print(l)
        return ','.join(l)
        
        

    def deserialize(self, dat):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not dat:return None
        data=dat.split(',')
        if not data:
            return None
        node=TreeNode(int(data[0]))
        
        q=deque()
        q.append(node)
        i=1
        while q and i<len(data):

            point=q.popleft()
            if data[i]!='#':
                point.left=TreeNode(int(data[i]))
                q.append(point.left)
            
            i+=1
            if i<len(data):
                if data[i]!='#':
                
                    point.right=TreeNode(int(data[i]))
                    q.append(point.right)
                
            i+=1
        return node


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))