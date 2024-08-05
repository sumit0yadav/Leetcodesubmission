"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:return root
        curr=root
        q=deque()
        q.append(curr)
        # print(q[0].val)
        while q:
            size=len(q)
            
            for i in range(size):
                node=q.popleft()

                if i==size-1:
                    node.next=None
                else:
                    node.next=q[0]
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return curr
                


        

        