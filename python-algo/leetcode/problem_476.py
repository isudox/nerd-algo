"""476. Number Complement
https://leetcode.com/problems/number-complement/
"""


class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        i = 0
        while num:
            bit = num & 0b1
            if bit == 0:
                ans += 1 << i
            num = num >> 1
            i += 1
        return ans
