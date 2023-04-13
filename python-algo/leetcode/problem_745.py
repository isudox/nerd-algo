"""745. Prefix and Suffix Search
https://leetcode.com/problems/prefix-and-suffix-search/
"""
from typing import List


class WordFilter:

    def __init__(self, words: List[str]):
        self.d = {}
        for i, word in enumerate(words):
            m = len(word)
            for prefix_length in range(1, m + 1):
                for suffix_length in range(1, m + 1):
                    self.d[word[:prefix_length] + '#' + word[-suffix_length:]] = i

    def f(self, pref: str, suff: str) -> int:
        return self.d.get(pref + '#' + suff, -1)
