"""1609. Even Odd Tree
https://leetcode.com/problems/even-odd-tree/
"""
from typing import Optional

from common.tree_node import TreeNode


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        store = [root]
        is_even_level = True
        while store:
            n = len(store)
            pre_val = None
            for i in range(n):
                node = store.pop(0)
                if is_even_level:
                    if node.val % 2 == 0:
                        return False
                    if pre_val:
                        if node.val <= pre_val:
                            return False
                else:
                    if node.val % 2 == 1:
                        return False
                    if pre_val:
                        if node.val >= pre_val:
                            return False
                pre_val = node.val
                if node.left:
                    store.append(node.left)
                if node.right:
                    store.append(node.right)
            is_even_level = not is_even_level
        return True
