"""104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

⁠   3
⁠  / \
⁠ 9  20
⁠   /  \
⁠  15   7

return its depth = 3.
"""
from common.tree_node import TreeNode


class Solution:
    def max_depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1
