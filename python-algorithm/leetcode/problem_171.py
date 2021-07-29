"""171. Excel Sheet Column Number
https://leetcode.com/problems/excel-sheet-column-number/
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        bit = 1
        for i in range(len(columnTitle) - 1, -1, -1):
            ans += (ord(columnTitle[i]) - 64) * bit
            bit *= 26
        return ans
