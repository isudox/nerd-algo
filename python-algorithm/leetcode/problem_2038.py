"""2038. Remove Colored Pieces if Both Neighbors are the Same Color
https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
"""


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)
        if n < 3:
            return False
        consecutives = {'A': 0, 'B': 0}
        i = 0
        while i < n:
            j = i
            while j < n and colors[j] == colors[i]:
                j += 1
            cnt = j - i
            if cnt >= 3:
                consecutives[colors[i]] += cnt - 2
            i = j
        return consecutives['A'] > consecutives['B']
