"""1015. Smallest Integer Divisible by K
https://leetcode.com/problems/smallest-integer-divisible-by-k/
"""


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return False
        num = 1
        ans = 1
        while True:
            if num % k == 0:
                break
            else:
                num = num * 10 + 1
                ans += 1
        return ans
