"""
https://leetcode.com/discuss/interview-experience/1844741/amazon-sde2-online-assesment
"""
from typing import List


class Solution:
    def countDecreasingRatings(self, ratings: List[int]) -> int:
        n = len(ratings)
        ans = 0
        i = 0
        while i < n:
            j = i + 1
            while j < n and ratings[j - 1] - ratings[j] == 1:
                j += 1
            ans += (j - i) * (j - i + 1) // 2
            i = j
        return ans
