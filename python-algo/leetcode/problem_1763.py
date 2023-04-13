"""1763. Longest Nice Substring
https://leetcode.com/problems/longest-nice-substring/
"""
from typing import List


def longest_nice_substring(s: str) -> str:
    def helper(l1: List[int], l2: List[int]) -> bool:
        for i in range(26):
            a, A = l2[i] - l1[i], l2[i + 32] - l1[i + 32],
            if (a == 0 and A != 0) or (a != 0 and A == 0):
                return False
        return True

    n = len(s)
    counter = [[0] * 128 for _ in range(n + 1)]
    for i in range(1, n + 1):
        counter[i] = counter[i - 1][:]
        counter[i][ord(s[i - 1]) - 65] += 1
    ans = ''
    for i in range(n):
        for j in range(i + 1, len(s)):
            if j - i + 1 <= len(ans):
                continue
            if helper(counter[i], counter[j + 1]):
                ans = s[i: j + 1]
    return ans
