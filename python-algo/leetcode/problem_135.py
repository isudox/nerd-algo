"""135. Candy
https://leetcode.com/problems/candy/
"""
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        def helper(start: int, end: int, step: int) -> List[int]:
            candies = [0] * n
            candies[start] = 1
            for i in range(start + step, end, step):
                if ratings[i] > ratings[i - step]:
                    candies[i] = candies[i - step] + 1
                else:
                    candies[i] = 1
            return candies
        n = len(ratings)
        candies_left = helper(0, n, 1)
        candies_right = helper(n - 1, -1, -1)
        ans = 0
        for i in range(n):
            ans += max(candies_left[i], candies_right[i])
        return ans
