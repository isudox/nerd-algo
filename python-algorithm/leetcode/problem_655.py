"""655. Print Binary Tree
https://leetcode.com/problems/print-binary-tree/
"""
from typing import List, Optional
from common.tree_node import TreeNode


class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def dfs(row: int, lo: int, hi: int, node: TreeNode) -> None:
            mid = (lo + hi) >> 1
            ans[row][mid] = str(node.val)
            if node.left:
                dfs(row + 1, lo, mid, node.left)
            if node.right:
                dfs(row + 1, mid + 1, hi, node.right)

        if not root:
            return []
        h = 0
        q = [root]
        while q:
            size = len(q)
            for _ in range(size):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            h += 1
        m, n = h, 2 ** h - 1
        ans = [[''] * n for _ in range(m)]
        dfs(0, 0, n, root)
        return ans
