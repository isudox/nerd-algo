"""1302. Deepest Leaves Sum
https://leetcode.com/problems/deepest-leaves-sum/
"""
from typing import Optional
from common.tree_node import TreeNode


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = [root]
        while q:
            ans = 0
            n = len(q)
            for _ in range(n):
                node = q.pop(0)
                ans += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not q:
                return ans
        return 0
