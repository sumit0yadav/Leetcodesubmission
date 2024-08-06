# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
# class Codec:

#     def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """

#         def h(node):
#             if not root:return ''
#             l=[]

#             q=deque()
#             q.append(node)

#             while q:
                
#                 curr=q.popleft()
#                 if curr:
#                     l.append(str(curr.val))
#                     q.append(curr.left)
#                     q.append(curr.right)
#                 else:
#                     l.append('#')
#             print(l)
#             return ''.join(l)
        
#         return h(root)

#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """
#         if len(data)==0:
#             return None
#         node=TreeNode(int(data[0]))
#         curr=node
#         q=deque()
#         q.append(curr)
#         i=1
#         while q and i<len(data):

#             point=q.popleft()
#             if data[i]!='#':
#                 point.left=TreeNode(int(data[i]))
#                 q.append(point.left)
            
#             i+=1
#             if i<len(data) and data[i]!='#':
                
#                 point.right=TreeNode(int(data[i]))
#                 q.append(point.right)
                
#             i+=1
#         return node

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        result = []
        q = deque([root])

        while q:
            node = q.popleft()
            if node:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                result.append("#")
        
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        i = 1

        while q and i < len(nodes):
            node = q.popleft()
            
            left_val = nodes[i]
            if left_val != "#":
                node.left = TreeNode(int(left_val))
                q.append(node.left)
            
            i += 1
            if i < len(nodes):
                right_val = nodes[i]
                if right_val != "#":
                    node.right = TreeNode(int(right_val))
                    q.append(node.right)
                
            i += 1

        return root


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))