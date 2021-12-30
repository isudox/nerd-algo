"""507. Perfect Number
https://leetcode.com/problems/perfect-number/
"""


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        summary = 1
        d = 2
        while d * d <= num:
            if num % d == 0:
                summary += d
                if d * d < num:
                    summary += num // d
            d += 1
        return summary == num
