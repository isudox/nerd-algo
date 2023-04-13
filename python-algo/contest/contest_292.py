import functools
from typing import Optional, List

from common.tree_node import TreeNode


# https://leetcode.com/contest/weekly-contest-292/
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ''
        cur = ''
        num += '#'
        for i in range(len(num)):
            if not cur or num[i] == cur[-1]:
                cur += num[i]
            else:
                if len(cur) >= 3:
                    cur = cur[:3]
                    if cur > ans:
                        ans = cur
                cur = num[i]
        return ans

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode):
            if not node:
                return [0, 0]
            ret = node.val
            cnt = 1
            left = dfs(node.left)
            right = dfs(node.right)
            ret += left[0] + right[0]
            cnt += left[1] + right[1]
            if ret // cnt == node.val:
                nonlocal ans
                ans += 1
            return [ret, cnt]

        ans = 0
        dfs(root)
        return ans

    def countTexts(self, pressedKeys: str) -> int:
        @functools.lru_cache(None)
        def helper(steps: int, total: int) -> int:
            if total == 0:
                return 1
            ret = 0
            for step in range(1, steps + 1):
                if step <= total:
                    ret += helper(steps, total - step)
                else:
                    break
            return ret % mod

        pressedKeys += '#'
        n = len(pressedKeys)
        l, r = 0, 0
        ans = 1
        mod = int(1e9 + 7)
        for i in range(n - 1):
            if pressedKeys[i] == pressedKeys[i + 1]:
                r += 1
            else:
                ret = helper(4, r - l + 1) if pressedKeys[i] in ('7', '9') else helper(3, r - l + 1)
                ans = ans * ret % mod
                l = r = i + 1
        return ans % mod

    def hasValidPath(self, grid: List[List[str]]) -> bool:
        def dfs(x: int, y: int, store: List[str]) -> bool:
            store2 = store[:]
            if x == m - 1 and y == n - 1:
                return True
            if grid[x][y] == ')':
                if not store2:
                    return False
                store2.pop()
                if x == m - 1 and y == n - 1 and not store2:
                    return True
            else:
                store2.append('(')
            for d in dirs:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < m and 0 <= ny < n:
                    if dfs(nx, ny, store2[:]):
                        return True
            return False

        if grid[0][0] == ')':
            return False
        m, n = len(grid), len(grid[0]),
        dirs = [[0, 1], [1, 0]]
        return dfs(0, 0, [])


if __name__ == '__main__':
    sol = Solution()
    print(sol.hasValidPath([["(", ")"], ["(", ")"]]))
