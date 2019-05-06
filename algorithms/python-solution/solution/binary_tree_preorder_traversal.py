"""144. Binary Tree Preorder Traversal
https://leetcode.com/problems/binary-tree-preorder-traversal/


Given a binary tree, return the pre-order traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import List

from common.tree_node import TreeNode


class Solution:

    def iterative_preorder_traversal(self, root: TreeNode) -> List[int]:
        pass

    def recursive_preorder_traversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = [root.val]
        ans += self.recursive_preorder_traversal(root.left)
        ans += self.recursive_preorder_traversal(root.right)
        return ans
