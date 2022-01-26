"""1688. Count of Matches in Tournament
https://leetcode.com/problems/count-of-matches-in-tournament/
"""


class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n > 1:
            a = n >> 1
            ans += a
            n -= a
        return ans
