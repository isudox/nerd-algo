"""2511. Maximum Enemy Forts That Can Be Captured
https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/
"""
from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        ans = 0
        pre_pos = pre_num = -9
        for i, num in enumerate(forts):
            if num == 0:
                continue
            if pre_num * num == -1:
                ans = max(ans, i - pre_pos - 1)
            pre_pos, pre_num = i, num
        return ans