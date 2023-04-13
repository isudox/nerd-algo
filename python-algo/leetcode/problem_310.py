"""310. Minimum Height Trees
https://leetcode.com/problems/minimum-height-trees/
"""
import collections
from typing import List


class Solution:
    def find_min_height_trees(self, n: int, edges: List[List[int]]) -> List[int]:
        def bfs(x: int) -> int:
            visited = [False] * n
            visited[x] = True
            q = collections.deque([x])
            cur = x
            while q:
                cur = q.popleft()
                for nxt in graph[cur]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        parents[nxt] = cur
                        q.append(nxt)
            return cur

        if n == 1:
            return [0]
        graph = collections.defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        parents = [0] * n
        x = bfs(0)
        y = bfs(x)
        path = []
        parents[x] = -1
        while y != -1:
            path.append(y)
            y = parents[y]
        dist = len(path)
        return [path[dist // 2]] if dist % 2 > 0 else [path[dist // 2 - 1], path[dist // 2]]
