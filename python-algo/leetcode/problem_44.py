"""44. Wildcard Matching
https://leetcode.com/problems/wildcard-matching/description/

Given an input string (s) and a pattern (p), implement wildcard pattern
matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like
? or *.

Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not
match 'b'.

Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*'
matches the substring "dce".

Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""


class Solution:
    def is_match(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        s_idx, p_idx = 0, 0
        p_star_idx = -1
        s_temp_idx = -1
        while s_idx < s_len:
            if p_idx == p_len or (
                p[p_idx] not in ["?", "*"] and p[p_idx] != s[s_idx]):
                if p_star_idx == -1:
                    return False
                else:
                    s_idx = s_temp_idx + 1
                    s_temp_idx = s_idx
                    p_idx = p_star_idx + 1
            elif p[p_idx] == s[s_idx] or p[p_idx] == "?":
                p_idx += 1
                s_idx += 1
            else:
                # "*" matches a sequence of characters increased from 0.
                p_star_idx = p_idx
                s_temp_idx = s_idx - 1
                p_idx += 1
        return all(x == "*" for x in p[p_idx:])

    def is_match_2(self, s: str, p: str) -> bool:
        """
        DP.
        Time complexity: O(mn)
        Space complexity: O(mn)
        """
        s_len, p_len = len(s), len(p)
        # dp[i][j] means if s[:i] and p[:j] matches.
        dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]
        dp[0][0] = True
        for i in range(1, p_len + 1):
            if p[i - 1] == '*':
                dp[0][i] = True
            else:
                break
        for i in range(1, s_len + 1):
            for j in range(1, p_len + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = False
        return dp[s_len][p_len]
