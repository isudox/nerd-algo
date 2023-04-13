"""1519. Number of Nodes in the Sub-Tree With the Same Label
https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/
"""
import collections
import functools
from typing import List


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        @functools.lru_cache(None)
        def dfs(cur: int, pre: int) -> List[int]:
            ret = [0] * 26
            for nxt in graph[cur]:
                if nxt != pre:
                    tmp = dfs(nxt, cur)
                    for i in range(26):
                        ret[i] += tmp[i]
            ret[ord(labels[cur]) - 97] += 1
            nonlocal ans
            ans[cur] = ret[ord(labels[cur]) - 97]
            return ret

        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        ans = [0] * n
        dfs(0, -1)
        return ans
