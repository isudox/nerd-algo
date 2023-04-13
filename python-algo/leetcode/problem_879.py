"""879. Profitable Schemes
https://leetcode.com/problems/profitable-schemes/

1 <= n <= 100
0 <= minProfit <= 100
1 <= group.length <= 100
1 <= group[i] <= 100
profit.length == group.length
0 <= profit[i] <= 100
"""
from typing import List
from functools import lru_cache


class Solution:
    def profitable_schemes(self, n: int, min_profit: int, group: List[int], profit: List[int]) -> int:
        @lru_cache(None)
        def dfs(i: int, left_workers: int, left_profit: int) -> int:
            if i == len(group):
                return 1 if left_profit == 0 else 0
            ret = 0
            job_workers, job_profit = pairs[i][0], pairs[i][1]
            if left_profit == 0:
                if left_workers >= job_workers:
                    ret += dfs(i + 1, left_workers - job_workers, 0)
                ret += dfs(i + 1, left_workers, 0)
            elif left_workers >= job_workers:
                ret += dfs(i + 1, left_workers - job_workers,
                           max(0, left_profit - job_profit))
                ret += dfs(i + 1, left_workers, left_profit)
            return ret % 1000000007

        pairs = list()
        for i in range(len(group)):
            pairs.append((group[i], profit[i]))
        pairs.sort(key=lambda x: x[0])
        return dfs(0, n, min_profit)

    def profitable_schemes2(self, n: int, min_profit: int, group: List[int], profit: List[int]) -> int:
        pairs = list()
        for i in range(len(group)):
            pairs.append((group[i], profit[i]))
        pairs.sort(key=lambda x: x[0])
        dp = [[[0] * (min_profit + 1) for _ in range(n + 1)] for _ in range(len(group) + 1)]
        for j in range(n + 1):
            dp[-1][j][0] = 1
        for i in range(len(group) - 1, -1, -1):
            job_workers, job_profit = pairs[i]
            for j in range(n + 1):
                for k in range(min_profit + 1):
                    if k == 0:
                        if j >= job_workers:
                            dp[i][j][k] += dp[i + 1][j - job_workers][0] % 1000000007
                        dp[i][j][k] += dp[i + 1][j][0] % 1000000007
                    elif j >= job_workers:
                        dp[i][j][k] += dp[i + 1][j - job_workers][max(0, k - job_profit)] % 1000000007
                        dp[i][j][k] += dp[i + 1][j][k] % 1000000007
        return dp[0][n][min_profit] % 1000000007

if __name__ == '__main__':
    sol = Solution()
    print(sol.profitable_schemes2(5,3,[2,2],[2,3]))
    print(sol.profitable_schemes2(10,5, [2,3,5], [6,7,8]))
