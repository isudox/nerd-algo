"""107. Binary Tree Level Order Traversal II
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

Given a binary tree, return the bottom-up level order traversal of its
nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]
"""
from typing import List

from common.tree_node import TreeNode


class Solution:
    def level_order_bottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = [root]
        cur_list = []
        next_queue = []
        while queue:
            node = queue.pop(0)
            cur_list.append(node.val)
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
            if not queue:
                ans.insert(0, cur_list)
                cur_list = []
                queue = next_queue
                next_queue = []

        return ans
