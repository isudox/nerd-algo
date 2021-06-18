"""483. Smallest Good Base
https://leetcode.com/problems/smallest-good-base/

Given an integer n represented as a string, return the smallest good base of
n.

We call k >= 2 a good base of n, if all digits of n base k are 1's.

Example 1:

Input: n = "13"
Output: "3"
Explanation: 13 base 3 is 111.

Example 2:

Input: n = "4681"
Output: "8"
Explanation: 4681 base 8 is 11111.

Example 3:

Input: n = "1000000000000000000"
Output: "999999999999999999"
Explanation: 1000000000000000000 base 999999999999999999 is 11.

Constraints:

n is an integer in the range [3, 10^18].
n does not contain any leading zeros.
"""


class Solution:
    def smallest_good_base(self, n: str) -> str:
        def cal(base: int, m: int) -> int:
            return (base ** m - 1) // (base - 1)

        n = int(n)
        maxsize = 59
        for size in range(maxsize, 1, -1):
            lo, hi = 2, int(n ** (1 / (size - 1)))
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                total = cal(mid, size)
                if total == n:
                    return str(mid)
                elif total < n:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return str(n - 1)
