"""32. Longest Valid Parentheses
https://leetcode.com/problems/longest-valid-parentheses/

Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""


class Solution:
    def longest_valid_parentheses(self, s: str) -> int:
        """
        stack
        time complexity: O(N)
        space complexity: O(N)
        """
        n = len(s)
        ans, cur = 0, 0
        stack = []
        for i in range(n):
            if s[i] == ')' and stack and s[stack[-1]] == '(':
                stack.pop()
                cur = i - stack[-1] if stack else i + 1
                ans = max(ans, cur)
            else:
                stack.append(i)
        return ans

    def longest_valid_parentheses_2(self, s: str) -> int:
        """
        dp
        time complexity: O(N)
        space complexity: O(N)
        """
        n = len(s)
        # dp[i] means the answer of the s[0, i]
        # if s[i-1, i] == '()', then dp[i] = dp[i-2] + 2
        # if s[i-1, i] == '))':
        # if s[i-1-dp[i-1]] == '(', then dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
        dp = [0] * n
        ans = 0
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    if i > 2:
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 2
                elif i - 1 - dp[i - 1] >= 0 and s[i - 1 - dp[i - 1]] == '(':
                    if i - dp[i - 1] > 2:
                        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                    else:
                        dp[i] = dp[i - 1] + 2
                ans = max(ans, dp[i])
        return ans
