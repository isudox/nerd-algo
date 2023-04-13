"""1238. Circular Permutation in Binary Representation
https://leetcode.com/problems/circular-permutation-in-binary-representation/
"""
from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        def next(x: int) -> int:
            y = x
            for i in range(n):
                if (x >> i) & 1 == 1:
                    z = y - (1 << i)
                else:
                    z = y + (1 << i)
                if not seen[z]:
                    return z
            return 0

        limit = 2 ** n
        seen = [False] * limit
        seen[start] = True
        ans = [start]
        for i in range(1, limit):
            tmp = next(ans[-1])
            seen[tmp] = True
            ans.append(tmp)
        return ans
