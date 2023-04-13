"""1022. Sum of Root To Leaf Binary Numbers
https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
"""
from typing import Optional

from common.tree_node import TreeNode


def sum_root_to_leaf(root: Optional[TreeNode]) -> int:
    def dfs(node: TreeNode, num: int):
        num = (num << 1) + node.val
        if not node.left and not node.right:
            nonlocal ans
            ans += num
            return
        if node.left:
            dfs(node.left, num)
        if node.right:
            dfs(node.right, num)

    if not root:
        return 0
    ans = 0
    dfs(root, 0)
    return ans
