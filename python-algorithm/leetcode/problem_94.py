"""94. Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/

Given a binary tree, return the in-order traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import List

from common.tree_node import TreeNode


class Solution:

    def iterative_inorder_traversal(self, root: TreeNode) -> List[int]:
        """
        iterative traversal
        :param root:
        :return:
        """
        ans = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                ans.append(root.val)
                root = root.right
        return ans

    def recursive_inorder_traversal(self, root: TreeNode) -> List[int]:
        """
        recursive traversal, process left if needed, then val, at last right
        :param root:
        :return:
        """
        if not root:
            return []
        ans = []
        ans += self.recursive_inorder_traversal(root.left)
        ans.append(root.val)
        ans += self.recursive_inorder_traversal(root.right)
        return ans
