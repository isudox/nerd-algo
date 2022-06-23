"""515. Find Largest Value in Each Tree Row
https://leetcode.com/problems/find-largest-value-in-each-tree-row/
"""
from typing import Optional
from typing import List
from common.tree_node import TreeNode


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        q = [root]
        while q:
            n = len(q)
            tmp = q[0].val
            for _ in range(n):
                node = q.pop(0)
                if node.val > tmp:
                    tmp = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(tmp)
        return ans
