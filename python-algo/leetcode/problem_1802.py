"""1802. Maximum Value at a Given Index in a Bounded Array
https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/
"""


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        lo, hi = 1, maxSum
        ans = 0
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            summ = mid
            if index < mid - 1:  # [...mid-2, mid-1]
                left_sum = (mid - 1 + (mid - index)) * index // 2
            else:  # [1,1,1 ...,mid-2,mid-1]
                left_sum = mid * (mid - 1) // 2 + index - (mid - 1)
            summ += left_sum
            if mid - 1 >= n - index - 1:  # [mid-1,mid-2, ..]
                right_sum = (mid - 1 + (mid - 1 - (n - index - 1) + 1)) * (n - index - 1) // 2
            else:  # [mid-1,mid-2,..,1,1,1]
                right_sum = mid * (mid - 1) // 2 + (n - index - 1) - (mid - 1)
            summ += right_sum
            if summ <= maxSum:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
