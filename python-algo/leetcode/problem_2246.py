"""2246. Longest Path With Different Adjacent Characters
https://leetcode.com/problems/longest-path-with-different-adjacent-characters/
"""
import collections
import functools
from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        @functools.lru_cache(None)
        def dfs(cur: int, pre: int) -> int:
            if pre != -1 and s[cur] == s[pre]:
                return 0
            ret = 1
            for nxt in graph[cur]:
                if nxt == pre:
                    continue
                ret = max(ret, dfs(nxt, cur) + 1)
            return ret

        graph = collections.defaultdict(list)
        for i, p in enumerate(parent):
            if p != -1:
                graph[p].append(i)
                graph[i].append(p)
        ans = 0
        for i in range(len(parent)):
            ans = max(ans, dfs(i, -1))
        return ans
