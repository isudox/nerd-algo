"""1449. Form Largest Integer With Digits That Add up to Target
https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/
"""
from functools import lru_cache
from typing import List


class Solution:
    def largest_number(self, cost: List[int], target: int) -> str:
        def compare(a: str, b: str) -> bool:
            return a > b if len(a) == len(b) else len(a) > len(b)

        @lru_cache(None)
        def dfs(x: int) -> str:
            if x == 0:
                return ''
            res = '0'
            for i in range(len(cost)):
                if cost[i] <= x:
                    ret = dfs(x - cost[i])
                    if ret != '0':
                        ret = str(i + 1) + ret
                        if compare(ret, res):
                            res = ret
            return res

        return dfs(target)

    def largest_number3(self, cost: List[int], target: int) -> str:
        def gt(a: str, b: str) -> bool:
            return a > b if len(a) == len(b) else len(a) > len(b)

        dp = [''] * (target + 1)
        for i in range(1, target + 1):
            dp[i] = '0'
            for j in range(9):
                if cost[j] <= i:
                    ret = dp[i - cost[j]]
                    if ret != '0':
                        ret = str(j + 1) + ret
                        if gt(ret, dp[i]):
                            dp[i] = ret
        return dp[target]

    def largest_number2(self, cost: List[int], target: int) -> str:
        def get_digits() -> int:
            for i in range(1, len(cost) + 1):
                for j in range(1, target + 1):
                    dp[i][j] = dp[i - 1][j]
                    if cost[i - 1] == j:
                        dp[i][j] = max(dp[i][j], 1)
                    elif cost[i - 1] < j and dp[i][j - cost[i - 1]] != 0:
                        dp[i][j] = max(dp[i][j], 1 + dp[i][j - cost[i - 1]])
            return dp[len(cost)][target]

        dp = [[0] * (target + 1) for _ in range(len(cost) + 1)]
        digits = get_digits()
        if digits <= 0:
            return '0'
        ans = ''
        for num in range(len(cost), 0, -1):
            c = cost[num - 1]
            while target >= c and dp[-1][target] == 1 + dp[-1][target - c]:
                if target == c:
                    return ans + str(num)
                elif dp[-1][target - c] != 0:
                    ans += str(num)
                    target -= c
                else:
                    break
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.largest_number2([4, 3, 2, 5, 6, 7, 2, 5, 5], 9))
    print(sol.largest_number3([4, 3, 2, 5, 6, 7, 2, 5, 5], 9))
