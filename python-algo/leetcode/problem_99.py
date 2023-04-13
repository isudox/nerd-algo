"""99. Recover Binary Search Tree
https://leetcode.com/problems/recover-binary-search-tree/

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2

Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3

Follow up:

    A solution using O(n) space is pretty straight forward.
    Could you devise a constant space solution?
"""
from typing import List

from common.tree_node import TreeNode


class Solution:
    def recover_tree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        swap_nums = []

        def ldr(node: TreeNode) -> List[int]:
            """
            in-order traversal.
            :return: List of int.
            """
            if not node:
                return []
            ret = []
            ret.extend(ldr(node.left))
            ret.append(node.val)
            ret.extend(ldr(node.right))
            return ret

        def recover(node: TreeNode) -> None:
            if node:
                if node.val == swap_nums[0]:
                    node.val = swap_nums[1]
                elif node.val == swap_nums[1]:
                    node.val = swap_nums[0]
                recover(node.left)
                recover(node.right)

        nums = ldr(root)
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                swap_nums.append(nums[i])

        recover(root)

    def recover_tree_2(self, root: TreeNode) -> None:
        def ldr(node: TreeNode, nums: List[int], nodes: List[TreeNode]) -> None:
            if not node:
                return
            ldr(node.left, nums, nodes)
            nums.append(node.val)
            nodes.append(node)
            ldr(node.right, nums, nodes)

        num_list = []
        node_list = []
        ldr(root, num_list, node_list)
        num_list.sort()
        for i in range(len(num_list)):
            node_list[i].val = num_list[i]
