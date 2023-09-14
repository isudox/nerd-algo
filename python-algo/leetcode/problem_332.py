"""332. Reconstruct Itinerary
https://leetcode.com/problems/reconstruct-itinerary/
"""
import collections
import heapq
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(cur: str):
            while g[cur]:
                nxt = heapq.heappop(g[cur])
                dfs(nxt)
            stk.append(cur)

        g = collections.defaultdict(list)
        for a, b in tickets:
            g[a].append(b)
        for k in g:
            heapq.heapify(g[k])
        stk = []
        dfs("JFK")
        return stk[::-1]
