"""678. Valid Parenthesis String
https://leetcode.com/problems/valid-parenthesis-string/
"""


class Solution:
    def check_valid_string(self, s: str) -> bool:
        left_stack, star_stack = [], []
        for i, c in enumerate(s):
            if c == '(':
                left_stack.append(i)
            elif c == '*':
                star_stack.append(i)
            else:
                if left_stack:
                    left_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        if len(left_stack) > len(star_stack):
            return False
        i, j = 0, len(star_stack) - len(left_stack)
        while i < len(left_stack):
            if left_stack[i] > star_stack[j]:
                return False
            i += 1
            j += 1
        return True
