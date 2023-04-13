"""257. Binary Tree Paths
https://leetcode.com/problems/binary-tree-paths/

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""
from typing import List

from common.tree_node import TreeNode


class Solution:
    def binary_tree_paths(self, root: TreeNode) -> List[str]:
        def dfs(node: TreeNode, path: str):
            if not node.left and not node.right:  # leaf node
                ans.append(path)
                return
            if node.left:
                dfs(node.left, path + '->' + str(node.left.val))
            if node.right:
                dfs(node.right, path + '->' + str(node.right.val))

        if not root:
            return []
        ans = []
        dfs(root, str(root.val))
        return ans
