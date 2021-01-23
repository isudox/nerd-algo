"""1319. Number of Operations to Make Network Connected
https://leetcode.com/problems/number-of-operations-to-make-network-connected/

Example 1:
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.

Example 2:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2

Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.

Example 4:

Input: n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
Output: 0

Constraints:

    1 <= n <= 10^5
    1 <= connections.length <= min(n*(n-1)/2, 10^5)
    connections[i].length == 2
    0 <= connections[i][0], connections[i][1] < n
    connections[i][0] != connections[i][1]
    There are no repeated connections.
    No two computers are connected by more than one cable.
"""
from typing import List


class Solution:
    def make_connected(self, n: int, connections: List[List[int]]) -> int:
        def union(x: int, y: int):
            fx, fy = find(x), find(y)
            if rank[fx] < rank[fy]:
                fx, fy = fy, fx
            uf[fy] = fx
            rank[fx] += rank[fy]

        def find(x: int) -> int:
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        if len(connections) < n - 1:
            return -1
        uf, rank, required = list(range(n)), [1] * n, 0
        for a, b in connections:
            if find(a) != find(b):
                union(a, b)
                required += 1
        return (n - 1) - required
