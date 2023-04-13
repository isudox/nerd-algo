"""337. House Robber III
https://leetcode.com/problems/house-robber-iii/

The thief has found himself a new place for his thievery again.
There is only one entrance to this area, called the "root." Besides the root,
each house has one and only one parent house. After a tour, the smart thief
realized that "all houses in this place forms a binary tree".
It will automatically contact the police if two directly-linked houses were
broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without
alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
"""
from common.tree_node import TreeNode


class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            if node in memo:
                return memo.get(node)
            temp1 = node.val
            if node.left:
                temp1 += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                temp1 += dfs(node.right.left) + dfs(node.right.right)
            temp2 = dfs(node.left) + dfs(node.right)
            memo[node] = max(temp1, temp2)
            return memo[node]

        memo = {}
        return dfs(root)
