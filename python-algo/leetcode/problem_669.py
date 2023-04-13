"""669. Trim a Binary Search Tree
https://leetcode.com/problems/trim-a-binary-search-tree/
"""
from typing import Optional
from common.tree_node import TreeNode


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        if low <= root.val <= high:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root
        if root.val < low:
            return self.trimBST(root.right, low, high)
        return self.trimBST(root.left, low, high)
