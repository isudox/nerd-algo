"""991. Broken Calculator
https://leetcode.com/problems/broken-calculator/
"""


class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        if startValue >= target:
            return startValue - target
        ans = 0
        if target <= startValue * 2:
            if target % 2 == 0:
                return min(startValue - target // 2, startValue * 2 - target) + 1
            return min(startValue * 2 - target + 1, self.brokenCalc(startValue, target + 1) + 1)
        while target > startValue * 2:
            if target % 2 == 0:
                target >>= 1
            else:
                target += 1
            ans += 1
        return ans + self.brokenCalc(startValue, target)
