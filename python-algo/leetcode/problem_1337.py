"""1337. The K Weakest Rows in a Matrix
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
"""
import collections
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def count(nums: List[int]) -> int:
            cnt = 0
            for num in nums:
                if num == 0:
                    break
                cnt += 1
            return cnt

        values = [False] * (len(mat[0]) + 1)
        store = collections.defaultdict(list)
        for i in range(len(mat)):
            cur = count(mat[i])
            store[cur].append(i)
            values[cur] = True
        ans = []
        for i, value in enumerate(values):
            if value:
                rows = store[i]
                for row in rows:
                    if k > 0:
                        ans.append(row)
                        k -= 1
        return ans
