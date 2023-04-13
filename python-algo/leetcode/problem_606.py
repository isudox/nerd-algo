"""606. Construct String from Binary Tree
https://leetcode.com/problems/construct-string-from-binary-tree/
"""
from typing import Optional

from common.tree_node import TreeNode


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node: TreeNode) -> str:
            if not node:
                return ""
            ret = str(node.val)
            if not node.left and not node.right:
                return ret
            if not node.left and node.right:
                return ret + '()(' + dfs(node.right) + ')'
            if node.left and not node.right:
                return ret + '(' + dfs(node.left) +')'
            else:
                return ret + '(' + dfs(node.left) +')' + '(' + dfs(node.right) + ')'
        return dfs(root)
