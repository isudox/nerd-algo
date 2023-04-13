"""1780. Check if Number is a Sum of Powers of Three
https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/
"""


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 3:
            n, b = divmod(n, 3)
            if b == 2:
                return False
        return n != 2
