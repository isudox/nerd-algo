"""687. Longest Univalue Path
https://leetcode.com/problems/longest-univalue-path/
"""
import functools
from typing import Optional, List

from common.tree_node import TreeNode


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        @functools.lru_cache(None)
        def helper(node: TreeNode) -> List[int]:
            if not node:
                return [0, 0]
            left = right = 0
            if node.left and node.left.val == node.val:
                left += max(helper(node.left)) + 1
            if node.right and node.right.val == node.val:
                right += max(helper(node.right)) + 1
            return [left, right]

        if not root:
            return 0
        ans = 0
        q = [root]
        while q:
            n = len(q)
            for _ in range(n):
                node = q.pop(0)
                cnt1, cnt2 = helper(node)
                ans = max(ans, cnt1 + cnt2)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans
