"""204. Count Primes
https://leetcode.com/problems/count-primes/

Count the number of prime numbers less than a non-negative number, n.

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:

Input: n = 0
Output: 0

Example 3:

Input: n = 1
Output: 0

Constraints:

0 <= n <= 5 * 10^6
"""


class Solution:
    def count_primes(self, n: int) -> int:
        store = [True] * n
        ans = 0
        for i in range(2, n):
            if store[i]:
                ans += 1
            j = 2 * i
            while j < n:
                store[j] = False
                j += i
        return ans
