"""6. ZigZag Conversion
https://leetcode.com/problems/zigzag-conversion/
"""


class Solution:
    def convert(self, s: str, rows: int) -> str:
        n = len(s)
        if rows == 1:
            return s
        x, y = divmod(n, 2 * rows - 2)
        cols = x * (rows - 1) + (1 if y <= rows else y - rows + 1)
        matrix = [[''] * cols for _ in range(rows)]
        i, j = 0, 0
        down = True
        for c in s:
            matrix[i][j] = c
            if i == rows - 1:
                down = False
            elif i == 0:
                down = True
            if down:
                i += 1
            else:
                i -= 1
                j += 1
        ans = ''
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] != '':
                    ans += matrix[row][col]
        return ans
