"""1189. Maximum Number of Balloons
https://leetcode.com/problems/maximum-number-of-balloons/
"""
import collections


def max_number_of_balloons(text: str) -> int:
    counter = collections.Counter(text)
    return min(counter['b'], counter['a'], counter['l'] // 2, counter['o'] // 2, counter['n'])
