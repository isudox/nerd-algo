"""987. Vertical Order Traversal of a Binary Tree
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
"""
import collections
from typing import List

from common.tree_node import TreeNode


class Solution:
    def vertical_traversal(self, root: TreeNode) -> List[List[int]]:
        def dfs(node: TreeNode, row: int, col: int):
            nonlocal max_row
            max_row = max(max_row, row)
            mapper[(row, col)].append(node.val)
            if node.left:
                dfs(node.left, row + 1, col - 1)
            if node.right:
                dfs(node.right, row + 1, col + 1)

        if not root:
            return []
        mapper = collections.defaultdict(list)
        max_row = 0
        dfs(root, 0, 0)
        sorted_columns = []
        for k, v in mapper.items():
            sorted_columns.append(k[1])
        sorted_columns.sort()
        visited_column = set()
        ans = []
        for column in sorted_columns:
            if column not in visited_column:
                visited_column.add(column)
                cur = []
                for i in range(max_row + 1):
                    key = (i, column)
                    if key in mapper:
                        mapper[key].sort()
                        cur.extend(mapper[key])
                if cur:
                    ans.append(cur)
        return ans
