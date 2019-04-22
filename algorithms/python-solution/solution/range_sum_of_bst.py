"""938. Range Sum of BST
https://leetcode.com/problems/range-sum-of-bst/

Given the root node of a binary search tree, return the sum of values of all
nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.




Example 1:


Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32



Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23




Note:


The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.
"""
from common.tree_node import TreeNode


class Solution:

    def range_sum_bst(self, root: TreeNode, l: int, r: int) -> int:
        """
        A nerd approach which doesn't use BST.
        :param root:
        :param l:
        :param r:
        :return:
        """
        if not root:
            return 0
        ans = 0
        if l <= root.val <= r:
            ans += root.val
        ans += self.range_sum_bst(root.left, l, r)
        ans += self.range_sum_bst(root.right, l, r)
        return ans

    def range_sum_bst_2(self, root: TreeNode, l: int, r: int) -> int:
        if not root:
            return 0
        ans = 0
        if root.val < l:
            ans += self.range_sum_bst_2(root.right, l, r)
        elif root.val > r:
            ans += self.range_sum_bst_2(root.left, l, r)
        else:
            ans += root.val
            ans += self.range_sum_bst_2(root.left, l, r)
            ans += self.range_sum_bst_2(root.right, l, r)
        return ans
