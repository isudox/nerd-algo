"""112. Path Sum
https://leetcode.com/problems/path-sum/

Given a binary tree and a sum, determine if the tree has a root-to-leaf path
such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""
from common.tree_node import TreeNode


class Solution:
    def has_path_sum(self, root: TreeNode, sum: int) -> bool:
        """
        recursive
        time complexity: O(N)
        space complexity: O(H), H is the height of tree.
        """
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        sum -= root.val
        if root.left and self.has_path_sum(root.left, sum):
            return True
        if root.right and self.has_path_sum(root.right, sum):
            return True
        return False
