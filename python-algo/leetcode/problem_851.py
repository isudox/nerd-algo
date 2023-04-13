"""851. Loud and Rich
https://leetcode.com/problems/loud-and-rich/
"""
import collections
from typing import List


def loud_and_rich(richer: List[List[int]], quiet: List[int]) -> List[int]:
    def dfs(x: int):
        # quietest person who is richer than person[p]
        if ans[x] > -1:
            return
        ans[x] = x
        for y in graph[x]:
            dfs(y)
            if quiet[ans[y]] < quiet[ans[i]]:
                ans[x] = ans[y]

    graph = collections.defaultdict(list)
    for x, y in richer:
        graph[y].append(x)  # all graph[y] are richer than y
    n = len(quiet)
    ans = [-1] * n
    for i in range(n):
        dfs(i)
    return ans
