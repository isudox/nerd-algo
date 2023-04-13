"""746. Min Cost Climbing Stairs
https://leetcode.com/problems/min-cost-climbing-stairs/

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps.
You need to find minimum cost to reach the top of the floor,
and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
"""
from typing import List


class Solution:
    def min_cost_climbing_stairs(self, cost: List[int]) -> int:
        # store whole dp elements.
        n = len(cost)
        if n == 2:
            return min(cost[0], cost[1])
        dp = [0 for _ in range(n + 1)]
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        return dp[-1]

    def min_cost_climbing_stairs_2(self, cost: List[int]) -> int:
        # only store last 2 dp elements.
        n = len(cost)
        if n == 2:
            return min(cost[0], cost[1])
        store = [0, 0]
        for i in range(2, n + 1):
            store = [store[1],
                     min(store[0] + cost[i - 2], store[1] + cost[i - 1])]
        return store[1]
