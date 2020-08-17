"""110. Balanced Binary Tree
https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in
height by no more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""
from common.tree_node import TreeNode


class Solution:
    def is_balanced(self, root: TreeNode) -> bool:
        def get_height(node: TreeNode) -> int:
            if node in memo:
                return memo.get(node)
            if not node:
                memo[node] = 0
                return 0
            memo[node] = max(get_height(node.left), get_height(node.right)) + 1
            return memo[node]

        def validate(node: TreeNode) -> bool:
            if not node:
                return True
            if abs(get_height(node.left) - get_height(node.right)) > 1:
                return False
            return validate(node.left) and validate(node.right)

        memo = {}
        return validate(root)
