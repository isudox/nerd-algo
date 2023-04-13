"""1711. Count Good Meals
https://leetcode.com/problems/count-good-meals/
输入：deliciousness = [1,1,1,3,3,3,7]
输出：15
解释：大餐的美味程度组合为 3 种 (1,1) ，9 种 (1,3) ，和 3 种 (1,7) 。
1 <= deliciousness.length <= 10^5
0 <= deliciousness[i] <= 2^20
"""
from typing import List
import collections
import math


class Solution:
    def count_pairs(self, deliciousness: List[int]) -> int:
        counter = collections.Counter()
        max_val = 0
        for ele in deliciousness:
            counter[ele] += 1
            max_val = max(max_val, ele)
        n = int(math.log2(max_val + max_val))
        store = set()
        ans = 0
        for num, cnt in counter.items():
            total = 0.5
            for i in range(n + 1):
                total = int(total * 2)
                if total - num == num:
                    ans += cnt * (cnt - 1) // 2 % 1000000007
                elif total - num in store:
                    ans += cnt * counter[total - num] % 1000000007
            store.add(num)
        return ans
