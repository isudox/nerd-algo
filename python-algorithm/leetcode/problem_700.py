"""700. Search in a Binary Search Tree
https://leetcode.com/problems/search-in-a-binary-search-tree/
"""
from common.tree_node import TreeNode


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if root.val < val:
            return self.searchBST(root.right, val)
        if root.val > val:
            return self.searchBST(root.left, val)
        return root
