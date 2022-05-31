"""269. Alien Dictionary
https://leetcode.com/problems/alien-dictionary/
"""
import collections
import itertools
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = collections.defaultdict(list)
        for s, t in itertools.pairwise(words):
            for u, v in zip(s, t):
                if u != v:
                    graph[u].append(v)
                    break
            else:
                if len(s) > len(t):
                    return ''
        states = {}
        order = []
