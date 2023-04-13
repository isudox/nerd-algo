"""543. Diameter of Binary Tree
https://leetcode.com/problems/diameter-of-binary-tree/

Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between
any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note:

The length of path between two nodes is represented by the number of
edges between them.
"""
from typing import List

from common.tree_node import TreeNode


class Solution:
    def diameter_of_binary_tree(self, root: TreeNode) -> int:
        memo = {}
        ans = 0

        def recur(node: TreeNode) -> List[int]:
            if not node:
                return [0, 0]
            if node in memo:
                return memo[node]
            cur_left, cur_right = 0, 0
            if node.left:
                cur_left = max(recur(node.left)) + 1
            if node.right:
                cur_right = max(recur(node.right)) + 1
            memo[node] = [cur_left, cur_right]
            nonlocal ans
            ans = max(ans, cur_left + cur_right)
            return memo[node]

        recur(root)
        return ans
