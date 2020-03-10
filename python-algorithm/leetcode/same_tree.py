"""100. Same Tree
https://leetcode.com/problems/same-tree/

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical
and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""
from typing import List

from common.tree_node import TreeNode


class Solution:
    def is_same_tree(self, p: TreeNode, q: TreeNode) -> bool:
        def traversal(node: TreeNode) -> List[int]:
            ret = []
            if node is None:
                return []
            ret.append(node.val)
            if node.left:
                ret.extend(traversal(node.left))
            else:
                ret.append(None)
            if node.right:
                ret.extend(traversal(node.right))
            else:
                ret.append(None)
            return ret

        return traversal(p) == traversal(q)
