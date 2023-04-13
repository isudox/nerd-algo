"""326. Power of Three
https://leetcode.com/problems/power-of-three/
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 1:
            return False
        n, m = divmod(n, 3)
        if m != 0:
            return False
        return self.isPowerOfThree(n)
