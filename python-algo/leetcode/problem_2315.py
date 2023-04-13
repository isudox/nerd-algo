"""2315. Count Asterisks
https://leetcode.com/problems/count-asterisks/
"""


class Solution:
    def countAsterisks(self, s: str) -> int:
        flag = False
        ans = 0
        for c in s:
            if c == '*':
                if not flag:
                    ans += 1
            elif c == '|':
                flag = not flag
        return ans
