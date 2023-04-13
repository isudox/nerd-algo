"""623. Add One Row to Tree
https://leetcode.com/problems/add-one-row-to-tree/
"""
from typing import Optional

from common.tree_node import TreeNode


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left=root)
        if not root:
            return None
        k = 1
        q = [root]
        while q:
            cur_level = q[:]
            next_level = []
            while q:
                node = q.pop(0)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if k == depth - 1:
                for node in cur_level:
                    left = node.left
                    node.left = TreeNode(val)
                    node.left.left = left
                    right = node.right
                    node.right = TreeNode(val)
                    node.right.right = right
            else:
                q = next_level
            k += 1
        return root
