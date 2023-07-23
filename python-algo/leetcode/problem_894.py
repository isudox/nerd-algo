"""894. All Possible Full Binary Trees
https://leetcode.com/problems/all-possible-full-binary-trees/
"""
from typing import List
from typing import Optional
from common.tree_node import TreeNode
import functools


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        @functools.cache
        def helper(m: int) -> List[Optional[TreeNode]]:
            if m == 2:
                return []
            if m == 1:
                return [TreeNode(0)]
            ret = []
            for i in range(1, m - 1):
                left = helper(i)
                right = helper(m - 1 - i)
                if not left or not right:
                    continue
                for l in left:
                    for r in right:
                        ret.append(TreeNode(0, l, r))
            return ret
        return helper(n)
