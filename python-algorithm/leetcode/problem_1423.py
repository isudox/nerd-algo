"""1423. Maximum Points You Can Obtain from Cards
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

Constraints:

    1 <= cardPoints.length <= 10^5
    1 <= cardPoints[i] <= 10^4
    1 <= k <= cardPoints.length
"""
from typing import List


class Solution:
    def max_score(self, card_points: List[int], k: int) -> int:
        n = len(card_points)
        card_points.extend(card_points)
        i, j = n - k, n
        ans = cur = sum(card_points[n - k:n])
        while j < n + k:
            cur += card_points[j] - card_points[i]
            if cur > ans:
                ans = cur
            j += 1
            i += 1
        return ans

    def max_score_2(self, card_points: List[int], k: int) -> int:
        i, j = 0, k - 1
        cur = ans = sum(card_points[:k])
        while j > -1:
            i -= 1
            cur += card_points[i] - card_points[j]
            j -= 1
            if cur > ans:
                ans = cur
        return ans
