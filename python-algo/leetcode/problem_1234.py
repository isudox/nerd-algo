"""1234. Replace the Substring for Balanced String
https://leetcode.com/problems/replace-the-substring-for-balanced-string/
"""
import collections


class Solution:
    def balancedString(self, s: str) -> int:
        def helper():
            return counter['Q'] == sz and counter['W'] == sz and counter['E'] == sz

        sz = len(s) // 4
        counter = collections.Counter(s)
        if helper():
            return True
        ans = len(s)
        j = 0
        for i, c in enumerate(s):
            while j < len(s) and not helper():
                counter[s[j]] -= 1
                j += 1
            if not helper():
                break
            ans = min(ans, j - i)
            counter[c] += 1
        return ans
