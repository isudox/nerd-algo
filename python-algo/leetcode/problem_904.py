"""904. Fruit Into Baskets
https://leetcode.com/problems/fruit-into-baskets/
"""
import collections
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt = collections.Counter()
        i, ans = 0, 0
        for j, fruit in enumerate(fruits):
            cnt[fruit] += 1
            while len(cnt) > 2:
                cnt[fruits[i]] -= 1
                if cnt[fruits[i]] == 0:
                    del cnt[fruits[i]]
                i += 1
            ans = max(ans, j - i + 1)
        return ans
