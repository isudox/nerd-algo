"""783. Minimum Distance Between BST Nodes
https://leetcode.com/problems/minimum-distance-between-bst-nodes/
"""
from typing import Optional
from common.tree_node import TreeNode


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode):
            if not node:
                return
            nonlocal ans
            if root.left:
                ans = min(ans, abs(root.val - root.left.val))
            if root.right:
                ans = min(ans, abs(root.val - root.right.val))
            dfs(root.left)
            dfs(root.right)

        ans = 100001
        dfs(root)
        return ans
