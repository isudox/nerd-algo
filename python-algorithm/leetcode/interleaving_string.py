"""97. Interleaving String
https://leetcode.com/problems/interleaving-string/

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
"""


class Solution:
    def is_interleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_len, s2_len = len(s1), len(s2)
        if s1_len + s2_len != len(s3):
            return False
        dp = [[False] * (s2_len + 1) for _ in range(s1_len + 1)]
        dp[0][0] = True
        for i in range(1, s2_len + 1):
            dp[0][i] = dp[0][i - 1] and s2[i - 1] == s3[i - 1]
        for i in range(1, s1_len + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for i in range(1, s1_len + 1):
            for j in range(1, s2_len + 1):
                dp[i][j] = (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]) or \
                           (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])
        return dp[s1_len][s2_len]

    def is_interleave_1(self, s1: str, s2: str, s3: str) -> bool:
        def dfs(s1_idx, s2_idx, s3_idx, store) -> bool:
            if s1_idx < s1_len and s2_idx < s2_len and s3_idx < s3_len:
                if store[s1_idx][s2_idx] is not None:
                    return store[s1_idx][s2_idx]
                store[s1_idx][s2_idx] = False
                if s3[s3_idx] == s1[s1_idx]:
                    if dfs(s1_idx + 1, s2_idx, s3_idx + 1, store):
                        store[s1_idx][s2_idx] = True
                if s3[s3_idx] == s2[s2_idx]:
                    if dfs(s1_idx, s2_idx + 1, s3_idx + 1, store):
                        store[s1_idx][s2_idx] = True
                return store[s1_idx][s2_idx]
            elif s1_idx == s1_len:
                return s2[s2_idx:] == s3[s3_idx:]
            elif s2_idx == s2_len:
                return s1[s1_idx:] == s3[s3_idx:]

        s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)
        if s1_len + s2_len != s3_len:
            return False
        return dfs(0, 0, 0, [[None] * s2_len for _ in range(s1_len)])

    def is_interleave_2(self, s1: str, s2: str, s3: str) -> bool:
        def dfs(s1_idx, s2_idx, s3_idx) -> bool:
            if s1_idx < s1_len and s2_idx < s2_len and s3_idx < s3_len:
                if s3[s3_idx] == s1[s1_idx]:
                    if dfs(s1_idx + 1, s2_idx, s3_idx + 1):
                        return True
                if s3[s3_idx] == s2[s2_idx]:
                    if dfs(s1_idx, s2_idx + 1, s3_idx + 1):
                        return True
                return dfs(s1_idx, s2_idx, s3_idx + 1)
            elif s1_idx == s1_len:
                return s2[s2_idx:] == s3[s3_idx:]
            elif s2_idx == s2_len:
                return s1[s1_idx:] == s3[s3_idx:]
            return False

        s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)
        if s1_len + s2_len != s3_len:
            return False
        return dfs(0, 0, 0)
