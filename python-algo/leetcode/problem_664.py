"""664. Strange Printer
https://leetcode.com/problems/strange-printer/
"""
import collections
import bisect


class Solution:
    def strange_printer(self, s: str) -> int:
        # remove the consecutive same char.
        ss = [c for i, c in enumerate(s) if i == 0 or s[i] != s[i - 1]]
        n = len(ss)
        dp = [[n] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if ss[j] == ss[i]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
        return dp[0][-1]

    def strange_printer2(self, s: str) -> int:
        # remove the consecutive same char.
        s = ''.join([c for i, c in enumerate(s) if i == 0 or s[i] != s[i - 1]])
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        pos_map = collections.defaultdict(list)
        for i, c in enumerate(s):
            pos_map[c].append(i)
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if j == i:
                    dp[i][j] = 1
                elif s[j] == s[i]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1] + 1
                    for pos in pos_map[s[j]] + pos_map[s[i]]:
                        if i <= pos < j:
                            dp[i][j] = min(dp[i][j],
                                           dp[i][pos] + dp[pos + 1][j])
        return dp[0][-1]

    def strange_printer3(self, s: str) -> int:
        s = ''.join([c for i, c in enumerate(s) if i == 0 or s[i] != s[i - 1]])
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        pos_map = collections.defaultdict(list)
        for i, c in enumerate(s):
            pos_map[c].append(i)
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if j == i:
                    dp[i][j] = 1
                elif s[j] == s[i]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1] + 1
                    idx = bisect.bisect_left(pos_map[s[j]], j)
                    for k in reversed(pos_map[s[j]][:idx]):
                        if k < i:
                            break
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
                    idx = bisect.bisect_left(pos_map[s[i]], i)
                    for k in pos_map[s[i]][idx:]:
                        if k >= j:
                            break
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
        return dp[0][-1]
