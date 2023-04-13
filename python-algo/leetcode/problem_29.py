"""29. Divide Two Integers
https://leetcode.com/problems/divide-two-integers/
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN, MAX = -2147483648, 2147483647
        if dividend == MIN:
            if divisor == 1:
                return MIN
            if divisor == -1:
                return MAX
        if divisor == MIN:
            return 1 if dividend == MIN else 0
        if dividend == 0:
            return 0
        rev = False
        if dividend > 0:
            dividend = -dividend
            rev = not rev
        if divisor > 0:
            divisor = -divisor
            rev = not rev

        def helper(y: int, z: int, x: int) -> bool:
            result, add = 0, y
            while z > 0:
                if (z & 1) == 1:
                    if result < x - add:
                        return False
                    result += add
                if z != 1:
                    if add < x - add:
                        return False
                    add += add
                z >>= 1
            return True

        lo, hi, ans = 1, MAX, 0
        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            check = helper(divisor, mid, dividend)
            if check:
                ans = mid
                # 注意溢出
                if mid == MAX:
                    break
                lo = mid + 1
            else:
                hi = mid - 1

        return -ans if rev else ans
