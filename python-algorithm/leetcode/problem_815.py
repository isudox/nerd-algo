"""815. Bus Routes
https://leetcode.com/problems/bus-routes/

Constraints:

1 <= routes.length <= 500.
1 <= routes[i].length <= 10^5
All the values of routes[i] are unique.
sum(routes[i].length) <= 10^5
0 <= routes[i][j] < 10^6
0 <= source, target < 10^6
"""
from typing import List
import collections


class Solution:
    def num_buses_to_destination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        bus_queue = []
        stop_buses = collections.defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                if stop == source:
                    bus_queue.append(i)
                stop_buses[stop].append(i)
        visited_buses = set()
        ans = 0
        while bus_queue:
            ans += 1
            n = len(bus_queue)
            for _ in range(n):
                cur_bus = bus_queue.pop(0)
                for stop in routes[cur_bus]:
                    if stop == target:
                        return ans
                    for bus in stop_buses[stop]:
                        if bus not in visited_buses:
                            bus_queue.append(bus)
                            visited_buses.add(bus)
        return -1
