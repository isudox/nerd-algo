"""161. One Edit Distance
https://leetcode-cn.com/problems/one-edit-distance/

Given two strings s and t, return true if they are both one
edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.

Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "", t = ""
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "a", t = ""
Output: true
Example 4:

Input: s = "", t = "A"
Output: true

Constraints:

0 <= s.length <= 10^4
0 <= t.length <= 10^4
s and t consist of lower-case letters, upper-case letters and/or digits.
"""


class Solution:
    def is_one_edit_distance(self, s: str, t: str) -> bool:
        """FAILED: TLE"""
        def dfs(x: int, y: int, edit: int) -> bool:
            if x == len(s):
                return y + edit == len(t)
            if y == len(t):
                return x + edit == len(s)
            if memo[x][y]:
                return memo[x][y]
            if s[x] == t[y]:
                memo[x][y] = dfs(x + 1, y + 1, edit)
            elif edit == 1:
                memo[x][y] = dfs(x, y + 1, 0) or dfs(x + 1, y, 0) or dfs(x + 1, y + 1, 0)
            else:
                memo[x][y] = False
            return memo[x][y]

        m, n = len(s), len(t)
        if abs(m - n) > 1:
            return False
        memo = [[None] * n for _ in range(m)]
        return dfs(0, 0, 1)

    def is_one_edit_distance2(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m > n:
            return self.is_one_edit_distance2(t, s)
        if n - m > 1:
            return False
        for i in range(m):
            if s[i] != t[i]:
                if m == n:
                    return s[i + 1:] == t[i + 1:]
                return s[i:] == t[i + 1:]
        return m != n
