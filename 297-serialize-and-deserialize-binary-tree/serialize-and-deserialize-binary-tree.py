# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None
# from collections import deque
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
#                 size=len(q)
#                 for _ in range(size):
#                     curr=q.popleft()
#                     if curr:
#                         l.append(curr.val)
#                         q.append(curr.left)
#                         q.append(curr.right)
#                     else:
#                         l.append('#')
#             return ''.join(map(str, l))
            
        

#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """
#         if len(data)==0:return None
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
#             else:
#                 point.left=None
#             i+=1
#             if data[i]!='#':
#                 point.right=TreeNode(int(data[i]))
#                 q.append(point.right)
#             else:
#                 point.right=None
#             i+=1
#         return node


        

# # Your Codec object will be instantiated and called as such:
# # ser = Codec()
# # deser = Codec()
# # ans = deser.deserialize(ser.serialize(root))
from collections import deque

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
            if nodes[i] != "#":
                node.left = TreeNode(int(nodes[i]))
                q.append(node.left)
            i += 1
            if i < len(nodes) and nodes[i] != "#":
                node.right = TreeNode(int(nodes[i]))
                q.append(node.right)
            i += 1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
