"""337. House Robber III
https://leetcode.com/problems/house-robber-iii/
"""
from common.tree_node import TreeNode
from typing import Optional
import functools


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @functools.cache
        def dfs(node: Optional[TreeNode], flag: bool) -> int:
            if not node:
                return 0
            ret = dfs(node.left, True) + dfs(node.right, True)
            if flag:
                ret = max(ret, dfs(node.left, False) + dfs(node.right, False) + node.val)
            return ret

        return max(dfs(root, True), dfs(root, False))
