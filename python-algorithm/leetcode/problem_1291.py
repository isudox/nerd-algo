"""1291. Sequential Digits
https://leetcode.com/problems/sequential-digits/
"""
from typing import List


def sequential_digits(low: int, high: int) -> List[int]:
    def helper(start: int, digits: int) -> List[int]:
        if start + digits > 10 or start > 10:
            return []
        if digits == 1:
            return list(range(start, 10))
        ret = []
        for i in range(start, 11 - digits):
            num = 0
            for j in range(digits):
                num = num * 10 + (i + j)
            ret.append(num)
        return ret

    digits_lo, digits_hi = len(str(low)), len(str(high))
    candidates = []
    for i in range(digits_lo, digits_hi + 1):
        candidates.extend(helper(1, i))
    ans = []
    for num in candidates:
        if low <= num <= high:
            ans.append(num)
    return ans
