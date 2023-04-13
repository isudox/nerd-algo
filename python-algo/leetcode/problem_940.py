"""940. Distinct Subsequences II
https://leetcode.com/problems/distinct-subsequences-ii/
"""


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        base = int(1e9 + 7)
        dp = [0] * 26
        for i in range(len(s)):
            cur = 0
            for pre in dp:
                cur = (cur + pre) % base
            dp[ord(s[i]) - 97] = cur + 1
        ans = 0
        for cnt in dp:
            ans = (ans + cnt) % base
        return ans
