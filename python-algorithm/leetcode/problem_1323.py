"""1323. Maximum 69 Number
https://leetcode.com/problems/maximum-69-number/
"""


class Solution:
    def maximum69Number(self, num: int) -> int:
        ns = str(num)
        for i, c in enumerate(ns):
            if c == '6':
                return num + 3 * 10 ** (len(ns) - 1 - i)
        return num
