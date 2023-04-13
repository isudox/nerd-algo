"""881. Boats to Save People
https://leetcode.com/problems/boats-to-save-people/
"""
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans = 0
        i, j = 0, len(people) - 1
        while i < j:
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            ans += 1
        if i == j:
            ans += 1
        return ans

