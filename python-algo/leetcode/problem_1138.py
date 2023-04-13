"""1138. Alphabet Board Path
https://leetcode.com/problems/alphabet-board-path/
"""


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        path = [divmod(ord(c) - 97, 5) for c in target]
        ans = ''
        x = y = 0
        for p in path:
            px, py = p[0], p[1]
            if px == 5 and py == 0:
                ans += 'L' * (y - py) + 'D' * (px - x) + '!'
                x, y = px, py
                continue
            if px > x:
                ans += 'D' * (px - x)
            else:
                ans += 'U' * (x - px)
            if py > y:
                ans += 'R' * (py - y)
            else:
                ans += 'L' * (y - py)
            ans += '!'
            x, y = px, py
        return ans
