"""17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
from typing import List


class Solution:
    def letter_combinations(self, digits: str) -> List[str]:
        mapper = {'2': ['a', 'b', 'c'],
                  '3': ['d', 'e', 'f'],
                  '4': ['g', 'h', 'i'],
                  '5': ['j', 'k', 'l'],
                  '6': ['m', 'n', 'o'],
                  '7': ['p', 'q', 'r', 's'],
                  '8': ['t', 'u', 'v'],
                  '9': ['w', 'x', 'y', 'z']}
        ans = []
        for digit in digits:
            if not ans:
                ans.extend(mapper[digit])
                continue
            next_comb = []
            for char in mapper[digit]:
                for prev in ans:
                    next_comb.append(prev + char)
            ans = next_comb
        return ans
