"""222. Count Complete Tree Nodes
https://leetcode.com/problems/count-complete-tree-nodes/

Given a complete binary tree, count the number of nodes.

Definition:
In a complete binary tree every level, except possibly the last,
is completely filled, and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""
from common.tree_node import TreeNode


class Solution:
    def count_nodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if not node:
                return
            nonlocal ans
            ans += 1
            dfs(node.left)
            dfs(node.right)

        ans = 0
        dfs(root)
        return ans
