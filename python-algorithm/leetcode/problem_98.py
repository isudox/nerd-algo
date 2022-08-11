"""98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than
the node's key.
- The right subtree of a node contains only nodes with keys greater than
the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:

⁠   2
⁠  / \
⁠ 1   3

Input: [2,1,3]
Output: true

Example 2:

⁠   5
⁠  / \
⁠ 1   4
/ \
3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""
from common.tree_node import TreeNode


class Solution:
    def is_valid_bst(self, root: TreeNode) -> bool:
        def dfs(node: TreeNode, minimum, maximum) -> bool:
            if not node:
                return True
            if minimum is not None and minimum >= node.val:
                return False
            if maximum is not None and maximum <= node.val:
                return False
            return dfs(node.left, minimum, node.val) and dfs(node.right,
                                                             node.val, maximum)

        return dfs(root, None, None)

    def is_valid_bst_inorder(self, root: TreeNode) -> bool:
        """
        BST's in-order traversal sequence must be incremental.
        :param root:
        :return:
        """
        stack = []
        prev = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev and prev.val >= root.val:
                return False
            prev = root
            root = root.right
        return True
