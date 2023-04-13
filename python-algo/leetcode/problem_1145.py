"""1145. Binary Tree Coloring Game
https://leetcode.com/problems/binary-tree-coloring-game/
"""
from typing import Optional

from common.tree_node import TreeNode


class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_cnt = dfs(node.left)
            right_cnt = dfs(node.right)
            if node.val == x:
                nonlocal lsz, rsz
                lsz, rsz = left_cnt, right_cnt
            return left_cnt + right_cnt + 1

        lsz = rsz = 0
        dfs(root)
        return max(lsz, rsz, n - 1 - lsz - rsz) * 2 > n
