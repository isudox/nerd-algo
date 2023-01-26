"""2359. Find Closest Node to Given Two Nodes
https://leetcode.com/problems/find-closest-node-to-given-two-nodes/
"""
from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def helper(start: int) -> List[int]:
            dist = [n] * n
            d = 0
            while start != -1 and dist[start] == n:
                dist[start] = d
                d += 1
                start = edges[start]
            return dist

        n = len(edges)
        dist1, dist2 = helper(node1), helper(node2)
        min_dist = n
        ans = -1
        for i in range(n):
            cur = max(dist1[i], dist2[i])
            if cur < min_dist:
                ans = i
                min_dist = cur
        return ans
