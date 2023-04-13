"""814. Binary Tree Pruning
https://leetcode.com/problems/binary-tree-pruning/
"""
from common.tree_node import TreeNode
from typing import Optional


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            a = dfs(node.left)
            if not a:
                node.left = None
            b = dfs(node.right)
            if not b:
                node.right = None
            if not (a or b):
                return node.val == 1
            return True

        dummy = TreeNode(1, left=root)
        dfs(dummy)
        return dummy.left
