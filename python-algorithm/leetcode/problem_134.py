"""134. Gas Station
https://leetcode.com/problems/gas-station/

Example 1:

Input:
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
      -2,-2,-2,3,3

Output: 3

Example 2:

Input:
gas  = [2,3,4]
cost = [3,4,3]

Output: -1
"""
from typing import List


class Solution:
    def can_complete_circuit(self, gas: List[int], cost: List[int]) -> int:
        def run_from(idx: int) -> bool:
            cur_gas, count = 0, 0
            while count < n:
                cur_gas += gas[idx]
                if cur_gas < cost[idx]:
                    return False
                cur_gas -= cost[idx]
                count += 1
                idx = idx + 1 if idx != n - 1 else 0
            return True

        n = len(gas)
        starts = []
        for i in range(n):
            if gas[i] >= cost[i]:
                starts.append(i)
        for start in starts:
            if run_from(start):
                return start
        return -1

    def can_complete_circuit_2(self, gas: List[int], cost: List[int]) -> int:
        def greedy(idx: int) -> bool:
            cur_gas, count = 0, 0
            while count < n:
                cur_gas += gas[idx]
                if cur_gas < cost[idx]:
                    return False
                cur_gas -= cost[idx]
                if cur_gas < memo[idx]:
                    return False
                memo[idx] = cur_gas
                count += 1
                idx = idx + 1 if idx != n - 1 else 0
            return True

        n = len(gas)
        starts = []
        for i in range(n):
            if gas[i] - cost[i] >= 0:
                starts.append(i)
        memo = [-1] * n
        for start in starts:
            if greedy(start):
                return start
        return -1
