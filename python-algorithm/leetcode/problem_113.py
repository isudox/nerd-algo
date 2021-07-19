"""113. Path Sum II
https://leetcode.com/problems/path-sum-ii/
"""
from typing import List
from common.tree_node import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def dfs(node: TreeNode, target: int, path: List[int]):
            path.append(node.val)
            if not node.left and not node.right:
                if node.val == target:
                    ans.append(path[:])
            if node.left:
                dfs(node.left, target - node.val, path)
            if node.right:
                dfs(node.right, target - node.val, path)
            path.pop()
        if not root:
            return []
        ans = []
        dfs(root, targetSum, [])
        return ans