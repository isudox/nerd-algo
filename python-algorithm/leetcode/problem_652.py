"""652. Find Duplicate Subtrees
https://leetcode.com/problems/find-duplicate-subtrees/
"""
from typing import List
from typing import Optional
from common.tree_node import TreeNode
import collections


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def dfs(node: Optional[TreeNode]) -> str:
            if not node:
                return ''
            left, right = dfs(node.left), dfs(node.right)
            key = '{}-{}-{}'.format(str(node.val), left, right)
            if store[key] == 1:
                ans.append(node)
            store[key] += 1
            return key

        store = collections.defaultdict(int)
        ans = []
        dfs(root)
        return ans
