"""100. Same Tree
https://leetcode.com/problems/same-tree/
"""
from typing import List

from common.tree_node import TreeNode


class Solution:
    def is_same_tree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        stk0, stk1 = [p], [q]
        while stk0 and stk1:
            if len(stk0) != len(stk1):
                return False
            n = len(stk0)
            for i in range(n):
                node0, node1 = stk0.pop(0), stk1.pop(0)
                if node0.val != node1.val:
                    return False
                if (node0.left and not node1.left) or (node1.left and not node0.left):
                    return False
                if node0.left:
                    stk0.append(node0.left)
                if node0.right:
                    stk0.append(node0.right)
                if node1.left:
                    stk1.append(node1.left)
                if node1.right:
                    stk1.append(node1.right)
        return len(stk0) == len(stk1)


