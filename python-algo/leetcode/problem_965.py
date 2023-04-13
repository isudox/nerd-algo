"""965. Univalued Binary Tree
https://leetcode.com/problems/univalued-binary-tree/

A binary tree is univalued if every node in the tree has the same value.
Return true if and only if the given tree is univalued.

Example 1:
  https://assets.leetcode.com/uploads/2018/12/28/unival_bst_1.png
  Input: [1,1,1,1,1,null,1]
  Output: true

Example 2:
  https://assets.leetcode.com/uploads/2018/12/28/unival_bst_2.png
  Input: [2,2,2,5,2]
  Output: false

Note:
  The number of nodes in the given tree will be in the range [1, 100].
  Each node's value will be an integer in the range [0, 99].
"""
from common.tree_node import TreeNode


class Solution:
    def is_unival_tree(self, root: 'TreeNode') -> 'bool':
        if root.val is None:
            return False

        value = root.val

        def recursive(node: 'TreeNode'):
            nonlocal value
            if node is None:
                return True
            if node.val != value:
                return False
            return recursive(node.left) and recursive(node.right)

        return recursive(root)
