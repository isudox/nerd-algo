"""1448. Count Good Nodes in Binary Tree
https://leetcode.com/problems/count-good-nodes-in-binary-tree/
"""
from common.tree_node import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, maxx: int):
            ret = 0
            if node.val >= maxx:
                ret += 1
            maxx = max(maxx, node.val)
            if node.left:
                ret += dfs(node.left, maxx)
            if node.right:
                ret += dfs(node.right, maxx)
            return ret

        return dfs(root, -1000000)
