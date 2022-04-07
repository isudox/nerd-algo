"""

"""


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        m, n = len(s), len(goal),
        if m != n:
            return False
        for i in range(m):
            if s[i:] + s[:i] == goal:
                return True
        return False
