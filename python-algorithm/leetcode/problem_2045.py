"""2045. Second Minimum Time to Reach Destination
https://leetcode.com/problems/second-minimum-time-to-reach-destination/
"""
import collections
from typing import List


def second_minimum(n: int, edges: List[List[int]], time: int, change: int) -> int:
    graph = collections.defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    dist = [[float('inf')] * 2 for _ in range(n + 1)]
    dist[1][0] = 0
    q = [(1, 0)]
    while dist[n][1] == float('inf'):
        p = q.pop(0)
        for np in graph[p[0]]:
            d = p[1] + 1
            if d < dist[np][0]:
                dist[np][0] = d
                q.append((np, d))
            elif dist[np][0] < d < dist[np][1]:
                dist[np][1] = d
                q.append((np, d))
    ans = 0
    for _ in range(dist[n][1]):
        rem = ans % (change + change)
        if rem >= change:
            ans += change + change - rem
        ans += time
    return ans
