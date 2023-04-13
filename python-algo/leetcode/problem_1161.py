"""1161. Maximum Level Sum of a Binary Tree
https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
"""
from typing import Optional

from common.tree_node import TreeNode


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans, summ, level = 1, root.val, 1
        q = [root]
        while q:
            cur = 0
            n = len(q)
            for _ in range(n):
                node = q.pop(0)
                cur += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if cur > summ:
                summ = cur
                ans = level
            level += 1
        return ans
