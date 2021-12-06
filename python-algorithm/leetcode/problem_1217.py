"""1217. Minimum Cost to Move Chips to The Same Position
https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
"""
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        cnt = [0, 0]
        for pos in position:
            cnt[pos % 2] += 1
        return min(cnt)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minCostToMoveChips([1, 2, 3]))
