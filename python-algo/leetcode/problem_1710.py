"""1710. Maximum Units on a Truck
https://leetcode.cn/problems/maximum-units-on-a-truck/description/
"""
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        ans = 0
        i = 0
        while truckSize > 0 and i < len(boxTypes):
            cnt = min(truckSize, boxTypes[i][0])
            ans += cnt * boxTypes[i][1]
            truckSize -= cnt
            i += 1
        return ans
