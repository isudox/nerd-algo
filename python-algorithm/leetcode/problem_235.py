"""235. Lowest Common Ancestor of a Binary Search Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
"""
from typing import List
from common.tree_node import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def helper(node: TreeNode, target: TreeNode, path: List[TreeNode]) -> bool:
            if not node:
                return False
            path.append(node)
            if node.val == target.val:
                nonlocal paths
                paths.append(path[::-1])
                return True
            if node.val < target.val:
                if helper(node.right, target, path):
                    return True
                path.pop()
            if node.val > target.val:
                if helper(node.left, target, path):
                    return True
                path.pop()
            return False

        paths = []
        helper(root, p, [])
        helper(root, q, [])
        node_set = set(paths[0])
        for i in range(len(paths[1])):
            if paths[1][i] in node_set:
                return paths[1][i]
        return None
