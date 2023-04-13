"""1539. Kth Missing Positive Number
https://leetcode.com/problems/kth-missing-positive-number/
"""
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        num = 1
        i = 0
        cnt = 0
        while i < len(arr):
            if num == arr[i]:
                num += 1
                i += 1
            else:
                cnt += 1
                if cnt == k:
                    return num
                num += 1
        return num + k - cnt - 1
