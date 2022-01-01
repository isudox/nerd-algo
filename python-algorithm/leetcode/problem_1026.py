"""1026. Maximum Difference Between Node and Ancestor
https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
"""
from typing import Optional

from common.tree_node import TreeNode


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, cur_max: int, cur_min: int):
            if not node:
                return
            nonlocal ans
            ans = max(ans, abs(node.val - cur_max), abs(node.val - cur_min))
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            dfs(node.left, cur_max, cur_min)
            dfs(node.right, cur_max, cur_min)

        if not root:
            return 0
        ans = 0
        dfs(root, root.val, root.val)
        return ans
