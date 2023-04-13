"""1614.
https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
"""


def max_depth(s: str) -> int:
    ans = 0
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            ans = max(ans, len(stack))
            stack.pop()
    return ans
