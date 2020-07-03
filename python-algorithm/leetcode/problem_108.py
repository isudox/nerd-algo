"""108. Convert Sorted Array to Binary Search Tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Given an array where elements are sorted in ascending order,
convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in
which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5],
which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""
from typing import List

from common.tree_node import TreeNode


class Solution:
    def sorted_array_to_bst(self, nums: List[int]) -> TreeNode:
        """
        recursive
        time complexity: O(N)
        space complexity: O(1)
        """

        def recur(start: int, end: int) -> TreeNode:
            # [start, end)
            if end == start:
                return None
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = recur(start, mid)
            root.right = recur(mid + 1, end)
            return root

        return recur(0, len(nums))
