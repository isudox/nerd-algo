"""168. Excel Sheet Column Title
https://leetcode.com/problems/excel-sheet-column-title/
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ''
        while columnNumber:
            columnNumber, rem = divmod(columnNumber, 26)
            if rem == 0:
                ans = 'Z' + ans
                columnNumber -= 1
            else:
                ans = chr(64 + rem) + ans
        return ans
