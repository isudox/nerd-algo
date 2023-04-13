"""22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/
"""
from typing import List


class Solution:
    def generate_parenthesis(self, n: int) -> List[str]:
        def gen(cur: str, left: int, right: int):
            if left == 0 and right == 0:
                ans.append(cur)
            if left > 0:
                gen(cur + '(', left - 1, right + 1)
            if right > 0:
                gen(cur + ')', left, right - 1)

        ans = []
        gen('', n, 0)
        return ans
