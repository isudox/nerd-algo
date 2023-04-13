"""530. Minimum Absolute Difference in BST
https://leetcode.com/problems/minimum-absolute-difference-in-bst/
"""
from typing import Optional, List

from common.tree_node import TreeNode


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = []
        ans = 100001
        pre = -1
        nums = []
        while root or q:
            while root:
                q.append(root)
                root = root.left
            node = q.pop()
            nums.append(node.val)
            if pre >= 0:
                ans = min(ans, node.val - pre)
            pre = node.val
            if node.right:
                root = node.right
        return ans
