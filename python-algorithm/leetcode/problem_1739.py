"""1739. Building Boxes
https://leetcode.com/problems/building-boxes/
"""


class Solution:
    def minimumBoxes(self, n: int) -> int:
        cur = i = j = 1
        while cur < n:
            n -= cur
            i += 1
            cur += i
        cur = 1
        while cur < n:
            n -= cur
            j += 1
            cur += 1
        return (i - 1) * i // 2 + j
