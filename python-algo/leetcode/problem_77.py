"""77. Combinations
https://leetcode.com/problems/combinations/
"""
from typing import List


class Solution:
    def combine_1(self, n: int, k: int) -> List[List[int]]:
        ans = [[_] for _ in range(1, n - k + 2)]
        for i in range(2, k + 1):
            temp = []
            for comb in ans:
                for j in range(comb[-1] + 1, n + 1):
                    new_comb = comb[:]
                    new_comb.append(j)
                    temp.append(new_comb)
            ans = temp
        return ans

    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        combine(n, k) = (combine(n-1, k-1) + n) + combine(n-1, k)
        """
        if k == 1:
            return [[_] for _ in range(1, n + 1)]
        if n == k:
            return [[_ for _ in range(1, n + 1)]]
        ans = self.combine(n - 1, k - 1)
        for comb in ans:
            comb.append(n)
        if n > k:
            ans.extend(self.combine(n - 1, k))
        return ans

    def combine_2(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start: int, comb: List[int]):
            for x in range(start, n + 1):
                # avoid unnecessary processing.
                if n - x + 1 < k - len(comb):
                    return
                temp = comb[:]
                temp.append(x)
                if len(temp) == k:
                    ans.append(temp)
                else:
                    backtrack(x + 1, temp)

        ans = []
        backtrack(1, [])
        return ans
