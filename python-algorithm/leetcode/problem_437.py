"""437. Path Sum III
https://leetcode.com/problems/path-sum-iii/

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf,
but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range
-1,000,000 to 1,000,000.

Example:
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""
from common.tree_node import TreeNode
from typing import List


class Solution:
    def path_sum(self, root: TreeNode, target: int) -> int:
        def recur(node: TreeNode, t: List[int]):
            nonlocal ans
            if not node:
                return
            for ele in t:
                if ele == node.val:
                    ans += 1
            t = [x - node.val for x in t]
            t.append(target)
            if node.left:
                recur(node.left, t)
            if node.right:
                recur(node.right, t)

        ans = 0
        recur(root, [target])
        return ans
