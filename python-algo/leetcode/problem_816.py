"""816. Ambiguous Coordinates
https://leetcode.com/problems/ambiguous-coordinates/
"""
from typing import List


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def helper(start: int, end: int) -> List[str]:
            ret = []
            if start == end or s[start] != '0':
                ret.append(s[start:end + 1])
            for i in range(start, end):
                a, b = s[start:i + 1], s[i + 1:end + 1]
                if len(a) > 1 and a[0] == '0':
                    continue
                if b[-1] == '0':
                    continue
                ret.append(f'{a}.{b}')
            return ret

        s = s[1:len(s) - 1]
        ans = []
        for i in range(len(s) - 1):
            x, y = helper(0, i), helper(i + 1, len(s) - 1)
            for xx in x:
                for yy in y:
                    ans.append(f'({xx}, {yy})')
        return ans
