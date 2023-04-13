"""2180. Count Integers With Even Digit Sum
https://leetcode.com/problems/count-integers-with-even-digit-sum/
"""


class Solution:
    def countEven(self, num: int) -> int:
        ans = 0
        for i in range(num, 0, -1):
            cur = 0
            while i:
                i, rem = divmod(i, 10)
                cur += rem
            if cur % 2 == 0:
                ans += 1
        return ans
