"""787. Cheapest Flights Within K Stops
https://leetcode.com/problems/cheapest-flights-within-k-stops/
"""
from functools import lru_cache
from typing import List


class Solution:
    def find_cheapest_price(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        @lru_cache(None)
        def dfs(pos: int, cnt: int) -> int:
            if cnt - 1 > k or (cnt - 1 == k and pos != dst):
                return float('inf')
            if pos == dst:
                return 0
            cost = float('inf')
            for next_path in paths[pos]:
                if next_path[0] == dst:
                    cost = min(cost, next_path[1])
                else:
                    cost = min(cost, next_path[1] + dfs(next_path[0], cnt + 1))
            return cost

        paths = [[] for _ in range(n)]
        for a, b, c in flights:
            paths[a].append([b, c])
        ans = dfs(src, 0)
        return ans if ans < float('inf') else -1
