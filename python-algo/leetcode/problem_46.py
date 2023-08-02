"""46. Permutations
https://leetcode.com/problems/permutations/
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = [[nums[0]]]
        for i in range(1, len(nums)):
            n = len(ans)
            for _ in range(n):
                perm = ans.pop(0)
                for j in range(i + 1):
                    cur = perm[:]
                    cur.insert(j, nums[i])
                    ans.append(cur)
        return ans
