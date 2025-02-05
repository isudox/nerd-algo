"""104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""
from common.tree_node import TreeNode


class Solution:
    def max_depth(self, root: TreeNode|None) -> int:
        if not root:
            return 0
        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1
    def max_depth2(self, root: TreeNode) -> int:
        # bfs
        if not root:
            return 0
        ans = 0
        q = [root]
        while q:
            n = len(q)
            for _ in range(n):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans += 1
        return ans
