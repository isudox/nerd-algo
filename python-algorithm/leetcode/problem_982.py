"""982. Triples with Bitwise AND Equal To Zero
https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/
"""
import collections
from typing import List


class Solution:
    def count_triplets(self, a: List[int]) -> int:
        ans = 0
        store = collections.Counter()
        for x in a:
            for y in a:
                store[x & y] += 1
        for z in a:
            for k, cnt in store.items():
                if k & z == 0:
                    ans += cnt
        return ans

    def count_triplets2(self, nums: List[int]) -> int:
        def count(x: int, y: int, z: int) -> int:
            if x == y == z:
                return 1
            if x == y or x == z or y == z:
                return 3
            return 6

        ans = 0
        bin_nums = [[0] * 16 for _ in range(len(nums))]
        for i in range(len(nums)):
            j = 0
            while nums[i]:
                bin_nums[i][j] = nums[i] & 1
                nums[i] = nums[i] >> 1
                j += 1

        for i in range(16):
            for j in range(len(nums)):
                pass
        return ans
