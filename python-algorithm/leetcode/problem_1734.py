"""1734. Decode XORed Permutation
https://leetcode.com/problems/decode-xored-permutation/

There is an integer array perm that is a permutation of the first n positive
integers, where n is always odd.

It was encoded into another integer array encoded of length n - 1, such that
encoded[i] = perm[i] XOR perm[i + 1]. For example, if perm = [1,3,2], then
encoded = [2,1].

Given the encoded array, return the original array perm. It is guaranteed
that the answer exists and is unique.

Example 1:

Input: encoded = [3,1]
Output: [1,2,3]
Explanation: If perm = [1,2,3], then encoded = [1 XOR 2,2 XOR 3] = [3,1]

Example 2:

Input: encoded = [6,5,4,6]
Output: [2,4,1,5,3]

Constraints:

3 <= n < 10^5
n is odd.
encoded.length == n - 1
"""
from typing import List


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        total = 0
        for i in range(1, n + 1):
            total = total ^ i
        ans = [total]
        for i in range(1, n - 1, 2):
            ans[0] = ans[0] ^ encoded[i]
        for i in range(n - 1):
            ans.append(ans[-1] ^ encoded[i])
        return ans

    def decode2(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        # https://www.geeksforgeeks.org/calculate-xor-1-n/
        total = 1 if n % 4 == 1 else 0
        for i in range(1, n - 1, 2):
            total ^= encoded[i]
        ans = [total]
        for i in range(n - 1):
            ans.append(ans[i] ^ encoded[i])
        return ans
