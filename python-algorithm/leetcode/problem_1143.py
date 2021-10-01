"""1143. Longest Common Subsequence
https://leetcode.com/problems/longest-common-subsequence/
"""
from functools import lru_cache


class Solution:
    def longest_common_subsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # dp[i][j] means the longest common subs of text1[0,i] and text2[0,j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

    def longest_common_subsequence2(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def dfs(i: int, j: int) -> int:
            if i == len(text1) or j == len(text2):
                return 0
            ret = 0
            if text1[i] == text2[j]:
                ret = 1 + dfs(i + 1, j + 1)
            ret = max(ret, dfs(i, j + 1))
            ret = max(ret, dfs(i + 1, j))
            return ret

        return dfs(0, 0)


if __name__ == '__main__':
    sol = Solution()
    print(sol.longest_common_subsequence("abcde", "ace"))
    print(sol.longest_common_subsequence(text1="abc", text2="abc"))
    print(sol.longest_common_subsequence(text1="abc", text2="def"))
