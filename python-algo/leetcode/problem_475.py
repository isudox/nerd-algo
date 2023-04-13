"""

"""
import bisect
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        ans = 0
        heaters.sort()
        for house in houses:
            j = bisect.bisect_right(heaters, house)
            i = j - 1
            right_distance = heaters[j] - house if j < len(heaters) else float('inf')
            left_distance = house - heaters[i] if i >= 0 else float('inf')
            cur = min(left_distance, right_distance)
            ans = max(ans, cur)
        return ans
