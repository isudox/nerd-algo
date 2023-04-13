"""403. Frog Jump
https://leetcode.com/problems/frog-jump/

A frog is crossing a river. The river is divided into some number of units,
and at each unit, there may or may not exist a stone. The frog can jump on a
stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order,
determine if the frog can cross the river by landing on the last stone.
Initially, the frog is on the first stone and assumes the first jump must be
1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k,
or k + 1 units. The frog can only jump in the forward direction.

Example 1:

Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd
stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3
units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th
stone.

Example 2:

Input: stones = [0,1,2,3,4,8,9,11]
Output: false
Explanation: There is no way to jump to the last stone as the gap between the
5th and 6th stone is too large.

Constraints:

2 <= stones.length <= 2000
0 <= stones[i] <= 2^31 - 1
stones[0] == 0
"""
from typing import List


class Solution:
    def can_cross(self, stones: List[int]) -> bool:
        n = len(stones)
        for i in range(1, n):
            if stones[i] - stones[i - 1] > i:
                return False
        dp = [[False] * n for _ in range(n)]
        dp[0][0] = True
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                jump = stones[i] - stones[j]
                if jump > j + 1:
                    break
                dp[i][jump] = dp[j][jump - 1] or dp[j][jump] or dp[j][jump + 1]
                if i == n - 1 and dp[i][jump]:
                    return True
        return False

    def can_cross_1(self, stones: List[int]) -> bool:
        """maximum recursion depth error"""

        def dfs(idx: int, jump: int):
            if jump in memo[idx]:
                return memo[idx].get(jump)
            if idx == len(stones) - 1:
                memo[idx][jump] = True
                return True
            ret = False
            for next_jump in range(max(1, jump - 1), jump + 2):
                stone = stones[idx] + next_jump
                for i in range(idx + 1, len(stones)):
                    if stones[i] == stone:
                        ret |= dfs(i, next_jump)
                    elif stones[i] > stone:
                        break
            memo[idx][jump] = ret
            return ret

        memo = [dict() for _ in range(len(stones))]
        ans = dfs(0, 0)
        return ans

    def can_cross_2(self, stones: List[int]) -> bool:
        """time limit exceeded"""
        dp = [set() for _ in range(len(stones))]
        dp[0].add(0)
        for i in range(1, len(stones)):
            for j in range(i - 1, -1, -1):
                if dp[j]:
                    need_jump = stones[i] - stones[j]
                    for jump in dp[j]:
                        if jump - 1 <= need_jump <= jump + 1:
                            dp[i].add(need_jump)
        return len(dp[-1]) > 0
