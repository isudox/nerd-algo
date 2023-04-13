"""235. Lowest Common Ancestor of a Binary Search Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
"""
from typing import List
from common.tree_node import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            return self.lowestCommonAncestor(root, q, p)
        while root:
            if p.val <= root.val <= q.val:
                return root
            if root.val > q.val:
                root = root.left
            else:
                root = root.right
        return None
