"""637. Average of Levels in Binary Tree
Given a non-empty binary tree, return the average value of the nodes
on each level in the form of an array.

Example 1:

Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

Note:

The range of node's value is in the range of 32-bit signed integer.
"""
from typing import List

from common.tree_node import TreeNode


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = [root]
        ans = []
        cur_sum, counter = 0, 0
        next_queue = []
        while queue:
            node = queue.pop(0)
            counter += 1
            cur_sum += node.val
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
            if not queue:
                ans.append(cur_sum / counter)
                queue = next_queue
                next_queue = []
                counter = 0
                cur_sum = 0
        return ans
