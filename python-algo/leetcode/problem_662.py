"""662. Maximum Width of Binary Tree
https://leetcode.com/problems/maximum-width-of-binary-tree/
"""
from typing import Optional

from common.tree_node import TreeNode


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = [(root, 0)]
        ans = 0
        while q:
            begin = False
            start = end = 0
            n = len(q)
            for _ in range(n):
                node, i = q.pop(0)
                if not node:
                    continue
                if not begin:
                    begin = True
                    start = i
                end = i
                if node.left:
                    q.append((node.left, 2 * i))
                if node.right:
                    q.append((node.right, 2 * i + 1))
            ans = max(ans, end - start + 1)
        return ans
