"""962. Maximum Width Ramp
https://leetcode.com/problems/maximum-width-ramp/

Given an array A of integers, a ramp is a tuple (i, j) for which
i < j and A[i] <= A[j].  The width of such a ramp is j - i.

Find the maximum width of a ramp in A.  If one doesn't exist, return 0.



Example 1:

Input: [6,0,8,2,1,5]
Output: 4
Explanation:
The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.

Example 2:

Input: [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation:
The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.

Note:

2 <= A.length <= 50000
0 <= A[i] <= 50000
"""
import bisect
from typing import List


class Solution:
    def max_width_ramp(self, a: List[int]) -> int:
        ramp, size = 0, len(a)
        candidates = [(a[size-1], size-1)]
        # candidates: i's decreasing, by increasing value of a[i]
        for i in range(size - 2, -1, -1):
            max_j = bisect.bisect(candidates, (a[i],))
            if max_j < len(candidates):
                ramp = max(ramp, candidates[max_j][1] - i)
            else:
                candidates.append((a[i], i))
        return ramp
