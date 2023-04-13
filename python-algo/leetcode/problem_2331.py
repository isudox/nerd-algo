"""2331. Evaluate Boolean Binary Tree
https://leetcode.com/problems/evaluate-boolean-binary-tree/
"""
from typing import Optional
from common.tree_node import TreeNode


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == 1
        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)
        if root.val == 2:
            return left or right
        return left and right
