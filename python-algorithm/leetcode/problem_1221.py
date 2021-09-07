"""1221. Split a String in Balanced Strings
https://leetcode.com/problems/split-a-string-in-balanced-strings/
"""


class Solution:
    def balanced_string_split(self, s: str) -> int:
        ans = 0
        cnt = {'L': 0, 'R': 0}
        for c in s:
            cnt[c] += 1
            if cnt['L'] == cnt['R']:
                ans += 1
                cnt = {'L': 0, 'R': 0}
        return ans
