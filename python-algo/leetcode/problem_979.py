"""979. Distribute Coins in Binary Tree
https://leetcode.com/problems/distribute-coins-in-binary-tree/
"""
from common.tree_node import TreeNode


class Solution:
    def distribute_coins(self, root: 'TreeNode') -> 'int':
        def dfs(node: TreeNode) -> int:
            nonlocal count
            if not node:
                return 0
            if not node.left and not node.right:
                count += abs(node.val - 1)
                return node.val - 1
            node.val += dfs(node.left)
            node.val += dfs(node.right)
            count += abs(node.val - 1)
            return node.val - 1

        count = 0
        dfs(root)
        return count
