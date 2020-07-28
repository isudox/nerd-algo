"""392. Is Subsequence
https://leetcode-cn.com/problems/is-subsequence/

Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original
string by deleting some (can be none) of the characters without disturbing the
relative positions of the remaining characters.
(ie, "ace" is a subsequence of "abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B,
and you want to check one by one to see if T has its subsequence.
In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 10^4
Both strings consists only of lowercase characters.
"""


class Solution:
    def is_subsequence(self, s: str, t: str) -> bool:
        """
        time complexity: O(M+N)
        space complexity: O(1)
        """
        if not s:
            return True
        len_s, len_t, index = len(s), len(t), 0
        for i in range(len_t):
            if t[i] == s[index]:
                index += 1
                if index == len_s:
                    return True
        return False

    def is_subsequence_2(self, s: str, t: str) -> bool:
        """
        dp
        time complexity: O(M*26+N)
        space complexity: O(m*26)
        """
        if not s:
            return True
        m, n = len(s), len(t)
        dp = [[0] * 26 for _ in range(n)]
        dp.append([-1] * 26)
        for i in range(n - 1, -1, -1):
            for j in range(26):
                if ord(t[i]) - ord('a') == j:
                    dp[i][j] = i
                else:
                    dp[i][j] = dp[i + 1][j]
        index = 0
        for i in range(m):
            index = dp[index][ord(s[i]) - ord('a')]
            if index == -1:
                return False
            else:
                index += 1
        return True
