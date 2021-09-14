"""1189. Maximum Number of Balloons
https://leetcode.com/problems/maximum-number-of-balloons/
"""
import collections


class Solution:
    def max_number_of_balloons(self, text: str) -> int:
        counter = collections.Counter()
        for c in text:
            if c in {'b', 'a', 'n'}:
                counter[c] += 2
            if c in {'o', 'l'}:
                counter[c] += 1
        ans = len(text)
        for key in ['b', 'a', 'l', 'o', 'n']:
            if counter[key] == 0:
                return 0
            if counter[key] < ans:
                ans = counter[key]
        return ans // 2
