"""1081. Smallest Subsequence of Distinct Characters
https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

Return the lexicographically smallest subsequence of s that contains all
the distinct characters of s exactly once.

Note: This question is the same as No.316

Example 1:

Input: s = "bcabc"
Output: "abc"

Example 2:

Input: s = "cbacdcbc"
Output: "acdb"

Constraints:

    1 <= s.length <= 1000
    s consists of lowercase English letters.
"""


class Solution:
    def smallest_subsequence(self, s: str) -> str:
        stack = []
        n = len(s)
        for i in range(n):
            c = s[i]
            if c in stack:
                continue
            while stack and stack[-1] > c and s.find(stack[-1], i) != -1:
                stack.pop()
            stack.append(c)
        return ''.join(stack)
