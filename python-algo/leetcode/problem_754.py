"""754. Reach a Number
https://leetcode.com/problems/reach-a-number/
"""


class Solution:
    def reachNumber(self, target: int) -> int:
        ans = 0
        target = abs(target)
        while target > 0:
            ans += 1
            target -= ans
        return ans if target % 2 == 0 else ans + 1 + ans % 2
