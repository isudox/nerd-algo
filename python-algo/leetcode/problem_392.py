"""392. Is Subsequence
https://leetcode-cn.com/problems/is-subsequence/
"""


class Solution:
    def is_subsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

    def is_subsequence_2(self, s: str, t: str) -> bool:
        """
        dp
        time complexity: O(M*26+N)
        space complexity: O(m*26)
        """
        if not s:
            return True
        m, n = len(s), len(t)
        dp = [[0] * 26 for _ in range(n)]
        dp.append([-1] * 26)
        for i in range(n - 1, -1, -1):
            for j in range(26):
                if ord(t[i]) - ord('a') == j:
                    dp[i][j] = i
                else:
                    dp[i][j] = dp[i + 1][j]
        index = 0
        for i in range(m):
            index = dp[index][ord(s[i]) - ord('a')]
            if index == -1:
                return False
            else:
                index += 1
        return True
