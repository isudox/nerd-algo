"""106. Construct Binary Tree from Inorder and Postorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal

Given two integer arrays inorder and postorder where inorder is the inorder
traversal of a binary tree and postorder is the postorder traversal of the
same tree, construct and return the binary tree.

Example 1:

    3
   / \
  9  20
    /  \
   15   7

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]

Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
"""
from common.tree_node import TreeNode
from typing import List


class Solution:
    def build_tree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        root = TreeNode(postorder[-1])
        pos = inorder.index(root.val)
        l_inorder = inorder[:pos]
        r_inorder = inorder[pos + 1:]
        if l_inorder:
            root.left = self.build_tree(l_inorder, postorder[:len(l_inorder)])
        if r_inorder:
            root.right = self.build_tree(r_inorder, postorder[len(postorder) - len(r_inorder) - 1 : -1])
        return root
