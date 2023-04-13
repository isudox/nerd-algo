"""226. Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/
"""
from common.tree_node import TreeNode


class Solution:
    def invert_tree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        ans = TreeNode(root.val)
        ans.left = self.invert_tree(root.right)
        ans.right = self.invert_tree(root.left)
        return ans
