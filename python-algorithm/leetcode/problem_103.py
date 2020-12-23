"""103. Binary Tree Zigzag Level Order Traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Given a binary tree, return the zigzag level order traversal of
its nodes' values. (ie, from left to right, then right to left for
the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""
from typing import List
from common.tree_node import TreeNode


class Solution:
    def zigzag_level_order(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = [root]
        flag = True
        while queue:
            values = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if flag:
                    values.append(node.val)
                else:
                    values.insert(0, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(values)
            flag = not flag
        return ans
