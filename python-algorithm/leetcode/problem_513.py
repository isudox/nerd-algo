"""513.
"""
from typing import Optional
from common.tree_node import TreeNode


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        q = [root]
        while q:
            is_end = True
            n = len(q)
            leftmost = q[0]
            for i in range(n):
                node = q.pop(0)
                if node.left or node.right:
                    is_end = False
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if is_end:
                return leftmost.val
        return None
