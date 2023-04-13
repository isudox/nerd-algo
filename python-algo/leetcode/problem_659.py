"""659. Split Array into Consecutive Subsequences
https://leetcode.com/problems/split-array-into-consecutive-subsequences/
"""
from collections import Counter
from typing import List


class Solution:

    def is_possible(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        count_map, end_map = Counter(nums), Counter()
        for num in nums:
            cnt = count_map.get(num)
            if cnt > 0:
                prev_cnt = end_map.get(num - 1, 0)
                if prev_cnt > 0:
                    count_map[num] -= 1
                    end_map[num - 1] = prev_cnt - 1
                    end_map[num] = end_map.get(num, 0) + 1
                else:
                    cnt1 = count_map.get(num + 1, 0)
                    cnt2 = count_map.get(num + 2, 0)
                    if cnt1 == 0 or cnt2 == 0:
                        return False
                    count_map[num] -= 1
                    count_map[num + 1] -= 1
                    count_map[num + 2] -= 1
                    end_map[num + 2] = end_map.get(num + 2, 0) + 1
        return True
