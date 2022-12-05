"""1687. Delivering Boxes from Storage to Ports
https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/
"""
from typing import List


class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        def cost(x: int, y: int) -> int:
            ret = 2
            port = boxes[x - 1][0]
            while x < y:
                x += 1
                if boxes[x - 1][0] == port:
                    continue
                ret += 1
                port = boxes[x - 1][0]
            return ret

        n = len(boxes)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        q = []
        diff, weight = 0, 0
        for i in range(1, n + 1):
            cur = dp[i - 1] + 2
            diff += 1 if i >= 2 and boxes[i - 1][0] != boxes[i - 2][0] else 0
            weight += boxes[i - 1][1]
            while q and q[-1][1] + diff >= cur:
                q.pop()
            q.append([i, cur - diff, boxes[i - 1][1] - weight])
            while q and (q[0][0] <= i - maxBoxes or q[0][2] + weight > maxWeight):
                q.pop(0)
            dp[i] = q[0][1] + diff
        return dp[n]
