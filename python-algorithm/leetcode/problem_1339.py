"""1339. Maximum Product of Splitted Binary Tree
https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
"""
from typing import Optional

from common.tree_node import TreeNode


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            ret = node.val
            if node.left:
                ret += dfs(node.left)
            if node.right:
                ret += dfs(node.right)
            store[node] = ret
            return ret
        if not root:
            return 0
        store = {}
        dfs(root)
        ans = 0
        q = [root]
        while q:
            n = len(q)
            for _ in range(n):
                node = q.pop(0)
                if node.left:
                    ans = max(ans, store[node.left] * (store[root] - store[node.left]))
                    q.append(node.left)
                if node.right:
                    ans = max(ans, store[node.right] * (store[root] - store[node.right]))
                    q.append(node.right)
        return ans % int(1e9 + 7)
