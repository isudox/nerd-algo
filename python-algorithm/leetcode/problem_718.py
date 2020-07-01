"""718. Maximum Length of Repeated Subarray
https://leetcode.com/problems/maximum-length-of-repeated-subarray/

Given two integer arrays A and B, return the maximum length of an subarray
that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation:
The repeated subarray with maximum length is [3, 2, 1].


Note:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
"""
from typing import List


class Solution:
    def find_length(self, a: List[int], b: List[int]) -> int:
        def cur_max_len(a_offset: int, b_offset: int, total_len: int) -> int:
            res = 0
            cur = 0
            for i in range(total_len):
                if a[a_offset + i] == b[b_offset + i]:
                    cur += 1
                    res = max(res, cur)
                else:
                    cur = 0
            return res

        a_len, b_len = len(a), len(b)
        ans = 0
        for i in range(a_len):
            length = min(a_len - i, b_len)
            ans = max(ans, cur_max_len(i, 0, length))
        for i in range(b_len):
            length = min(b_len - i, a_len)
            ans = max(ans, cur_max_len(0, i, length))
        return ans
