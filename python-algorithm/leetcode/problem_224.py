"""224. Basic Calculator
https://leetcode.com/problems/basic-calculator/

Given a string s representing an expression, implement a basic calculator to
evaluate it.

Example 1:

Input: s = "1 + 1"
Output: 2

Example 2:

Input: s = " 2-1 + 2 "
Output: 3

Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

Constraints:

1 <= s.length <= 3 * 10^5
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
"""


class Solution:
    def calculate(self, s: str) -> int:
        stack, rev_stack = [], []
        i, n, ans = 0, len(s), 0
        while i < n:
            if s[i] == ' ':
                i += 1
                continue
            if s[i].isnumeric():
                num = ''
                while s[i].isnumeric():
                    num += s[i]
                    i += 1
                stack.append(int(num))
            elif s[i] == ')':
                while stack[-1] != '(':
                    rev_stack.append(stack.pop())
                stack.pop()
                cur = 0
                while rev_stack:
                    top = rev_stack.pop()
                    if isinstance(top, int):
                        cur += top
                    elif top == '+':
                        cur += rev_stack.pop()
                    elif top == '-':
                        cur -= rev_stack.pop()
                stack.append(cur)
                i += 1
            else:
                stack.append(s[i])
                i += 1
        while stack:
            top = stack.pop(0)
            if isinstance(top, int):
                ans += top
            elif top == '+':
                ans += stack.pop(0)
            elif top == '-':
                ans -= stack.pop(0)
        return ans

    def calculate_2(self, s: str) -> int:
        def helper(expr, x: int) -> int:
            ret = 0
            while len(expr) > x:
                ele = expr.pop(x)
                if isinstance(ele, int):
                    ret += ele
                else:
                    ret = ret + (expr.pop(x) if ele == '+' else - expr.pop(x))
            return ret

        stack = []
        i, n = 0, len(s)
        while i < n:
            if s[i] == ' ':
                i += 1
                continue
            if s[i].isnumeric():
                num = ''
                while i < n and s[i].isnumeric():
                    num += s[i]
                    i += 1
                stack.append(int(num))
            elif s[i] == ')':
                j = len(stack) - 1
                while j >= 0 and stack[j] != '(':
                    j -= 1
                cur = helper(stack, j + 1)
                stack.pop()
                stack.append(cur)
                i += 1
            else:
                stack.append(s[i])
                i += 1
        return helper(stack, 0)
