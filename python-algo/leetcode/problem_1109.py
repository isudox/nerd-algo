"""1109. Corporate Flight Bookings
https://leetcode.com/problems/corporate-flight-bookings/
"""
from typing import List


class Solution:
    def corp_flight_bookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * n
        for start, end, x in bookings:
            ans[start - 1] += x
            if end < n:
                ans[end] -= x
        for i in range(1, n):
            ans[i] += ans[i - 1]
        return ans
