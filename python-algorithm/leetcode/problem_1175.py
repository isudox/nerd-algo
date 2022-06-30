"""Prime Arrangements
https://leetcode.com/problems/prime-arrangements/
"""
import math


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def is_prime(num: int) -> bool:
            if num < 2:
                return False
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True

        mod = int(1e9 + 7)
        prime_cnt = 0
        for i in range(1, n + 1):
            if is_prime(i):
                prime_cnt += 1
        ans = 1
        for i in range(1, prime_cnt + 1):
            ans = ans * i % mod
        for i in range(1, n - prime_cnt + 1):
            ans = ans * i % mod
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.numPrimeArrangements(100))
