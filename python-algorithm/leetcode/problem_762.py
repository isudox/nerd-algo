"""762. Prime Number of Set Bits in Binary Representation
https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/
"""


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            y = 2
            while y * y <= x:
                if x % y == 0:
                    return False
                y += 1
            return True

        return sum(is_prime(x.bit_count()) for x in range(left, right + 1))
