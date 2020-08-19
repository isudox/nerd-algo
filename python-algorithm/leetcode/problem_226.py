"""226. Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""
from common.tree_node import TreeNode


class Solution:
    def invert_tree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        ans = TreeNode(root.val)
        ans.left = self.invert_tree(root.right)
        ans.right = self.invert_tree(root.left)
        return ans
