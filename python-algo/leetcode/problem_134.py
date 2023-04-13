"""134. Gas Station
https://leetcode.com/problems/gas-station/
"""
from typing import List


class Solution:
    def can_complete_circuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = 0
        while i < n:
            sum_gas, sum_cost = 0, 0
            count = 0
            while count < n:
                j = (i + count) % n
                sum_gas += gas[j]
                sum_cost += cost[j]
                if sum_gas < sum_cost:
                    break
                count += 1
            if count == n:
                return i
            i = i + count + 1
        return -1
