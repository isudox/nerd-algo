"""105. Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

Return the following binary tree:

⁠   3
⁠  / \
⁠ 9  20
⁠   /  \
⁠  15   7
"""
from typing import List

from common.tree_node import TreeNode


class Solution:
    def build_tree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        left_tree_inorder = inorder[:index]
        right_tree_inorder = inorder[index + 1:]
        left_tree_preorder = preorder[1: index + 1]
        right_tree_preorder = preorder[index + 1:]
        root.left = self.build_tree(left_tree_preorder, left_tree_inorder)
        root.right = self.build_tree(right_tree_preorder, right_tree_inorder)
        return root
