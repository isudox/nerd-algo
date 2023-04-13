"""102. Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

   3
  / \
 9  20
   /  \
  15   7

return its level order traversal as:

[
 [3],
 [9,20],
 [15,7]
]
"""
from typing import List

from common.tree_node import TreeNode


class Solution:
    def level_order(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = [root]
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level)
        return ans
