"""145. Binary Tree Postorder Traversal
https://leetcode.com/problems/binary-tree-postorder-traversal/


Given a binary tree, return the post-order traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import List

from common.tree_node import TreeNode


class Solution:

    def iterative_postorder_traversal(self, root: TreeNode) -> List[int]:
        pass

    def recursive_postorder_traversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        ans += self.recursive_postorder_traversal(root.left)
        ans += self.recursive_postorder_traversal(root.right)
        ans.append(root.val)
        return ans
