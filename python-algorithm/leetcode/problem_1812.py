"""1812. Determine Color of a Chessboard Square
https://leetcode.com/problems/determine-color-of-a-chessboard-square/
"""


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        r, c = coordinates[1], coordinates[0]
        return (ord(c) - ord('a') + int(r)) % 2 == 0
