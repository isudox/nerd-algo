"""987. Vertical Order Traversal of a Binary Tree
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
"""
import collections
from typing import List, Optional

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

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node: Optional[TreeNode], row: int, col: int) -> None:
            if not node:
                return
            if row not in grid:
                grid[row] = dict()
            if col not in grid[row]:
                grid[row][col] = []
            grid[row][col].append(node.val)
            nonlocal left, right, down
            left = min(left, col)
            right = max(right, col)
            down = max(down, row)
            if node.left:
                dfs(node.left, row + 1, col - 1)
            if node.right:
                dfs(node.right, row + 1, col + 1)

        if not root:
            return []
        grid = dict()
        left = right = down = 0
        dfs(root, 0, 0)
        ans = []
        for c in range(left, right + 1):
            cur = []
            for r in range(down + 1):
                if r not in grid or c not in grid[r]:
                    continue
                grid[r][c].sort()
                cur.extend(grid[r][c])
            if cur:
                ans.append(cur)
        return ans
