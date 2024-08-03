from collections import defaultdict, deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        node_list = []
        
        def bfs(root):
            q = deque([(root, 0, 0)]) # node, vertical, horizontal
            while q:
                node, x, y = q.popleft()
                if node:
                    node_list.append((x, y, node.val))
                    q.append((node.left, x - 1, y + 1))
                    q.append((node.right, x + 1, y + 1))
        
        bfs(root)
        
        # Sort by x (vertical), then by y (horizontal), then by node value
        node_list.sort()
        
        res = defaultdict(list)
        for x, y, value in node_list:
            res[x].append(value)
        
        return [res[x] for x in sorted(res)]
