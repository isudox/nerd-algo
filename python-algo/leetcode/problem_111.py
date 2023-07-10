"""111. Minimum Depth of Binary Tree
https://leetcode.com/problems/minimum-depth-of-binary-tree/

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from
the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""
from common.tree_node import TreeNode


class Solution:
    def min_depth(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            if node.left and not node.right:
                return 1 + dfs(node.left)
            if node.right and not node.left:
                return 1 + dfs(node.right)
            return min(dfs(node.left), dfs(node.right)) + 1

        return dfs(root)
    
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = [root]
        ans = 0
        while q:
            ans += 1
            n = len(q)
            for _ in range(n):
                node = q.pop(0)
                if not node.left and not node.right:
                    return ans
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans
