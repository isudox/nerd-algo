"""1653. Minimum Deletions to Make String Balanced
https://leetcode.cn/problems/minimum-deletions-to-make-string-balanced/
"""


class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans = deleted = s.count('a')
        for c in s:
            if c == 'a':
                deleted -= 1
            else:
                deleted += 1
            if deleted < ans:
                ans = deleted
        return ans
