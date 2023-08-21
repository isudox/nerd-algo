"""459. Repeated Substring Pattern
https://leetcode.com/problems/repeated-substring-pattern/
"""


class Solution:
    def repeated_substring_pattern_1(self, s: str) -> bool:
        return s in (s + s)[1:-1]

    def repeated_substring_pattern(self, s: str) -> bool:
        def validate(prefix: str, start: int) -> bool:
            if start == n:
                return True
            if s[start:].startswith(prefix):
                return validate(prefix, start + len(prefix))
            else:
                return False

        n = len(s)
        for x in range(n // 2, 0, -1):
            if n % x == 0:
                if validate(s[:x], 0):
                    return True
        return False
