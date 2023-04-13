"""2283. Check if Number Has Equal Digit Count and Digit Value
https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/
"""
import collections


class Solution:
    def digitCount(self, num: str) -> bool:
        counter = collections.Counter(num)
        for i, v in enumerate(num):
            if int(v) != counter[str(i)]:
                return False
        return True
