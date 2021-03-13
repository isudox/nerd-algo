"""227. Basic Calculator II
https://leetcode.com/problems/basic-calculator-ii/

Given a string s which represents an expression, evaluate this expression and
return its value.

The integer division should truncate toward zero.

Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1

Example 3:
Input: s = " 3+5 / 2 "
Output: 5

Constraints:

1 <= s.length <= 3 * 10^5
s consists of integers and operators ('+', '-', '*', '/') separated by some
number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range
[0, 2^31 - 1].
The answer is guaranteed to fit in a 32-bit integer.
1 <= s.length <= 3 * 10^5
"""


class Solution:
    def calculate(self, s: str) -> int:
        def next_num(x: int):
            i = x
            while i < n and not s[i].isnumeric():
                i += 1
            j = i
            while j < n and s[j].isnumeric():
                j += 1
            return int(s[i:j]), j

        stack = []
        i, n = 0, len(s)
        while i < n:
            if s[i] == " ":
                i += 1
                continue
            if s[i].isnumeric():
                num = ""
                while i < n and s[i].isnumeric():
                    num += s[i]
                    i += 1
                stack.append(int(num))
            elif s[i] in {"*", "/"}:
                left = stack.pop()
                right, j = next_num(i)
                num = (left * right) if s[i] == "*" else (left // right)
                stack.append(num)
                i = j
            else:
                stack.append(s[i])
                i += 1
        ans = 0
        while stack:
            ele = stack.pop(0)
            if isinstance(ele, int):
                ans += ele
            elif ele == "+":
                ans = ans + stack.pop(0)
            else:
                ans -= stack.pop(0)
        return ans
