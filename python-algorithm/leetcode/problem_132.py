"""132. Palindrome Partitioning II
https://leetcode.com/problems/palindrome-partitioning-ii/

Given a string s, partition s such that every substring of the partition is a
palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1
cut.

Example 2:

Input: s = "a"
Output: 0

Example 3:

Input: s = "ab"
Output: 1

Constraints:

1 <= s.length <= 2000
s consists of lower-case English letters only.
"""


class Solution:
    def min_cut(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        memo = [[False] * n for _ in range(n)]
        for i in range(n):
            cut = i
            for j in range(i + 1):
                if s[i] == s[j] and (j + 1 > i - 1 or memo[j + 1][i - 1]):
                    memo[j][i] = True
                    cut = 0 if j == 0 else min(cut, dp[j - 1] + 1)
            dp[i] = cut
        return dp[-1]
