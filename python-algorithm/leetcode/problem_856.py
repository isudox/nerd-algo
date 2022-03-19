"""856. Score of Parentheses
https://leetcode.com/problems/score-of-parentheses/
"""


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for ch in s:
            if ch == '(':
                stack.append(ch)
            else:
                cur = 0
                while stack[-1] != '(':
                    cur += int(stack.pop())
                cur = cur * 2 if cur > 0 else 1
                stack.pop()
                stack.append(str(cur))
        ans = 0
        while stack:
            ans += int(stack.pop())
        return ans
