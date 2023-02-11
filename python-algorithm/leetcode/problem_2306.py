"""2306. Naming a Company
https://leetcode.com/problems/naming-a-company/
"""
from typing import List


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        store = [set() for _ in range(26)]
        for idea in ideas:
            store[ord(idea[0]) - 97].add(idea[1:])
        ans = 0
        for i in range(25):
            for j in range(i + 1, 26):
                mutual_num = len(store[i] & store[j])
                ans += 2 * (len(store[i]) - mutual_num) * (len(store[j]) - mutual_num)
        return ans
