"""701. Insert into a Binary Search Tree
https://leetcode.com/problems/insert-into-a-binary-search-tree/
"""
from typing import Optional

from common.tree_node import TreeNode


def insert_into_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    def dfs(node: Optional[TreeNode]):
        if node.val < val:
            if not node.right:
                node.right = TreeNode(val)
            else:
                dfs(node.right)
        if node.val > val:
            if not node.left:
                node.left = TreeNode(val)
            else:
                dfs(node.left)

    if not root:
        return TreeNode(val)
    dfs(root)
    return root
