"""72. Edit Distance
https://leetcode.com/problems/edit-distance/
"""
from typing import List


class Solution:
    def min_distance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)
        # dp[i][j] is the min distance to convert word1[:i] to word2[:j]
        dp = [[-1] * (len2 + 1) for _ in range(len1 + 1)]
        for i in range(len2 + 1):
            # insert i characters
            dp[0][i] = i
        for j in range(len1 + 1):
            # delete j characters
            dp[j][0] = j
        # state-transition equation:
        # if word1[i] equals to word2[j], it doesn't need any operations;
        # otherwise it should insert a character based on dp[i][j-1],
        # or delete a character based on dp[i-1][j],
        # or replace a character based on dp[i-1][j-1].
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j],
                                   dp[i][j - 1]) + 1
        return dp[len1][len2]

    def brute_force(self, word1: str, word2: str) -> int:
        def dfs(w1: str, i: int, w2: str, j: int) -> int:
            if i == len(w1):
                return len(w2) - j
            if j == len(w2):
                return len(w1) - i
            if w1[i] == w2[j]:
                return dfs(w1, i + 1, w2, j + 1)
            else:
                return 1 + min(dfs(w1, i + 1, w2, j + 1), dfs(w1, i + 1, w2, j), dfs(w1, i, w2, j + 1))

        return dfs(word1, 0, word2, 0)

    def brute_force_with_memo(self, word1: str, word2: str) -> int:
        def dfs(w1: str, i: int, w2: str, j: int, memo: List[List[int]]) -> int:
            if memo[i][j] != -1:
                return memo[i][j]
            if i == len(w1):
                memo[i][j] = len(w2) - j
            elif j == len(w2):
                memo[i][j] = len(w1) - i
            elif w1[i] == w2[j]:
                memo[i][j] = dfs(w1, i + 1, w2, j + 1, memo)
            else:
                memo[i][j] = 1 + min(dfs(w1, i + 1, w2, j + 1, memo), dfs(w1, i + 1, w2, j, memo), dfs(w1, i, w2, j + 1, memo))
            return memo[i][j]

        memo = [[-1] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        return dfs(word1, 0, word2, 0, memo)

    def min_distance2(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i
        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1])
        return dp[0][0]
