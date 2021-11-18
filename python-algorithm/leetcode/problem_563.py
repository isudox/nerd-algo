"""563. Binary Tree Tilt
https://leetcode.com/problems/binary-tree-tilt/
"""
from common.tree_node import TreeNode


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            nonlocal ans
            ans += abs(left - right)
            return left + right + node.val

        ans = 0
        dfs(root)
        return ans
