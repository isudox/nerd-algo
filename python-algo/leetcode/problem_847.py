"""847. Shortest Path Visiting All Nodes
https://leetcode.com/problems/shortest-path-visiting-all-nodes/
"""
import collections
from typing import List


class Solution:
    def shortest_path_length(self, graph: List[List[int]]) -> int:
        n = len(graph)
        store = collections.deque((i, 1 << i, 0) for i in range(n))
        visited = {(i, 1 << i) for i in range(n)}
        ans = 0
        while store:
            u, bits, steps = store.popleft()
            if bits == (1 << n) - 1:
                return steps
            for v in graph[u]:
                mask = bits | (1 << v)
                if (v, mask) not in visited:
                    visited.add((v, mask))
                    store.append((v, mask, steps + 1))
        return ans
