"""8. String to Integer (atoi)
https://leetcode.com/problems/string-to-integer-atoi/
"""


class Solution:
    def my_atoi(self, str: str) -> int:
        is_neg = False
        start = False
        result = 0
        for c in str:
            if not start:
                if c == ' ':
                    continue
                if c == '-':
                    start = True
                    is_neg = True
                    continue
                if c == '+':
                    start = True
                    continue
                if '0' <= c <= '9':
                    start = True
                    result = result * 10 + int(c)
                    continue
                else:
                    break
            else:
                if '0' <= c <= '9':
                    result = result * 10 + int(c)
                else:
                    break
        if is_neg:
            result = max(-result, -2 ** 31)
        else:
            result = min(result, 2 ** 31 - 1)
        return result
