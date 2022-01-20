"""875. Koko Eating Bananas
https://leetcode.com/problems/koko-eating-bananas/
"""
import bisect
import math
from typing import List


def min_eating_speed(piles: List[int], h: int) -> int:
    def helper(k: int) -> bool:
        cnt = 0
        pos = bisect.bisect_left(piles, k)
        cnt += pos
        for i in range(pos, len(piles)):
            a, b = divmod(piles[i], k)
            cnt += a + (1 if b > 0 else 0)
            if cnt > h:
                return False
        return True

    total, max_k = 0, 0
    for p in piles:
        total += p
        max_k = max(max_k, p)
    min_k = math.ceil(total / h)
    piles.sort()
    while min_k < max_k:
        mid_k = min_k + (max_k - min_k) // 2
        if helper(mid_k):
            max_k = mid_k
        else:
            min_k = mid_k + 1
    return min_k
