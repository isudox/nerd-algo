"""1473. Paint House III
https://leetcode.com/problems/paint-house-iii/

There is a row of m houses in a small city, each house must be painted with
one of the n colors (labeled from 1 to n), some houses that have been painted
last summer should not be painted again.

A neighborhood is a maximal group of continuous houses that are painted with
the same color.

For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods [{1}, {2,2},
{3,3}, {2}, {1,1}].

Given an array houses, an m x n matrix cost and an integer target
where:

houses[i]: is the color of the house i, and 0 if the house is not painted
yet.
cost[i][j]: is the cost of paint the house i with the color j + 1.

Return the minimum cost of painting all the remaining houses in such a way
that there are exactly target neighborhoods. If it is not possible, return
-1.

Example 1:

Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m =
5, n = 2, target = 3
Output: 9
Explanation: Paint houses of this way [1,2,2,1,1]
This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.

Example 2:

Input: houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m =
5, n = 2, target = 3
Output: 11
Explanation: Some houses are already painted, Paint the houses of this way
[2,2,1,2,2]
This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}]. 
Cost of paint the first and last house (10 + 1) = 11.

Example 3:

Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[1,10],[10,1],[1,10]], m =
5, n = 2, target = 5
Output: 5

Example 4:

Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n
= 3, target = 3
Output: -1
Explanation: Houses are already painted with a total of 4 neighborhoods
[{3},{1},{2},{3}] different of target = 3.

Constraints:

m == houses.length == cost.length
n == cost[i].length
1 <= m <= 100
1 <= n <= 20
1 <= target <= m
0 <= houses[i] <= n
1 <= cost[i][j] <= 10^4
"""
from typing import List


class Solution:
    def min_cost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        def dfs(idx: int, need_blocks: int, pre_color: int):
            key = (idx, need_blocks, pre_color)
            if idx == m or need_blocks < 0 or m - idx < need_blocks:
                return 0 if need_blocks == 0 and idx == m else float('inf')
            if key not in dp:
                if houses[idx] == 0:
                    dp[key] = min(dfs(idx + 1, need_blocks - (color != pre_color), color) + cost[idx][color - 1] for color in range(1, n + 1))
                else:
                    dp[key] = dfs(idx + 1, need_blocks - (houses[idx] != pre_color), houses[idx])
            return dp[key]

        dp = dict()
        ans = dfs(0, target, -1)
        return ans if ans < float('inf') else -1

    def min_cost2(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # key: i-j-k, value: min cost. means that the min cost by painting houses[i] with color j to k blocks.
        dp = [[[float('inf')] * target for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if houses[i] == 0 or houses[i] == j + 1:
                    for k in range(target):
                        for pre_j in range(n):
                            if pre_j == j:
                                if i == 0 and k == 0:
                                    dp[i][j][k] = 0
                                elif i > 0:
                                    dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k])
                            elif i > 0 and k > 0:
                                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][pre_j][k - 1])
                        if dp[i][j][k] != float('inf') and houses[i] == 0:
                            dp[i][j][k] += cost[i][j]

        ans = min(dp[m - 1][j][target - 1] for j in range(n))
        return -1 if ans == float('inf') else ans

    def min_cost3(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = [[[float('inf')] * target for _ in range(n)] for _ in range(m)]
        if houses[0] == 0:
            for j in range(n):
                dp[0][j][0] = cost[0][j]
        else:
            dp[0][houses[0] - 1][0] = 0

        for i in range(1, m):
            for j in range(n):
                if houses[i] == 0 or houses[i] == j + 1:
                    cur_cost = cost[i][j] if houses[i] == 0 else 0
                    for k in range(target):
                        for pre_j in range(n):
                            if pre_j == j:
                                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k] + cur_cost)
                            elif k > 0:
                                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][pre_j][k - 1] + cur_cost)

        ans = min(dp[m - 1][j][target - 1] for j in range(n))
        return -1 if ans == float('inf') else ans

