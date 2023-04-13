"""124. Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some
starting node to any node in the tree along the parent-child connections.
The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

⁠      1
⁠     / \
⁠    2   3
Output: 6

Example 2:

Input: [-10,9,20,null,null,15,7]

    -10
    / \
    9  20
      /  \
     15   7
Output: 42
"""
from common.tree_node import TreeNode


class Solution:
    def max_path_sum(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            nonlocal ans
            ans = max(left + right + node.val, ans)
            return max(left, right) + node.val

        if not root:
            return 0
        ans = root.val
        dfs(root)
        return ans
