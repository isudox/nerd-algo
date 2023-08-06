"""860. Lemonade Change
https://leetcode.com/problems/lemonade-change/
"""
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        store = {5: 0, 10: 0}
        for bill in bills:
            if bill == 10:
                if not store[5]:
                    return False
                store[5] -= 1
            elif bill == 20:
                if store[10] and store[5]:
                    store[10] -= 1
                    store[5] -= 1
                elif store[5] >= 3:
                    store[5] -= 3
                else:
                    return False
            if bill < 20:
                store[bill] += 1
        return True