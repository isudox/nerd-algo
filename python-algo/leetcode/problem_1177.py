from typing import List

"""1177. Can Make Palindrome from Substring
https://leetcode.com/problems/can-make-palindrome-from-substring
"""


class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        count = [0] * (len(s) + 1)
        for i in range(len(s)):
            count[i + 1] = count[i] ^ (1 << (ord(s[i]) - 97))
        ans = []
        for l, r, k in queries:
            bits = (count[r + 1] ^ count[l]).bit_count()
            ans.append(bits <= k * 2 + 1)
        return ans
