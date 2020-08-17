"""114. Flatten Binary Tree to Linked List
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

⁠   1
⁠  / \
⁠ 2   5
⁠/ \   \
3   4   6

The flattened tree should look like:

1
⁠\
⁠ 2
⁠  \
⁠   3
⁠    \
⁠     4
⁠      \
⁠       5
⁠        \
⁠         6
"""
from common.tree_node import TreeNode


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        if not (root.left or root.right):
            return
        self.flatten(root.left)
        self.flatten(root.right)
        cur = root.left
        if not cur:
            return
        while cur.right:
            cur = cur.right
        cur.right = root.right
        root.right = root.left
        root.left = None
