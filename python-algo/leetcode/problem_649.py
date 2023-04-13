"""649. Dota2 Senate
https://leetcode.com/problems/dota2-senate/
"""
from typing import List
import bisect


class Solution:
    def predict_party_victory(self, senate: str) -> str:
        def disable(idx_list: List[int], start: int):
            idx = bisect.bisect_right(idx_list, start)
            for j in range(idx, len(idx_list)):
                if can_vote[idx_list[j]]:
                    can_vote[idx_list[j]] = False
                    del idx_list[j]
                    return
            for j in range(idx):
                if can_vote[idx_list[j]]:
                    can_vote[idx_list[j]] = False
                    del idx_list[j]
                    return

        n = len(senate)
        can_vote = [True] * n
        r_list, d_list = [], []
        for i in range(n):
            (r_list if senate[i] == 'R' else d_list).append(i)
        while True:
            for i in range(n):
                if not can_vote[i]:
                    continue
                disable(d_list if senate[i] == 'R' else r_list, i)
                if not r_list:
                    return 'Dire'
                if not d_list:
                    return 'Radiant'

    def predict_party_victory_2(self, senate: str) -> str:
        n = len(senate)
        r_list, d_list = [], []
        for i in range(n):
            (r_list if senate[i] == 'R' else d_list).append(i)
        while r_list and d_list:
            if r_list[0] < d_list[0]:
                r_list.append(r_list[0] + n)
            else:
                d_list.append(d_list[0] + n)
            del r_list[0]
            del d_list[0]
        return 'Radiant' if r_list else 'Dire'
