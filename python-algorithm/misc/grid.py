class Solution:
    def count(self, m: int, n: int) -> int:
        dp0 = [[0] * n for _ in range(m)]
        dp1 = [[0] * n for _ in range(m)]
        dp0[0][0] = 1
        dp1[0][0] = 0
        for i in range(m):
            for j in range(n):
                for r in range(i):
                    dp0[i][j] += dp1[r][j]
                    dp1[i][j] += dp0[r][j]
                for c in range(j):
                    dp0[i][j] += dp1[i][c]
                    dp1[i][j] += dp0[i][c]
        return dp1[-1][-1]
