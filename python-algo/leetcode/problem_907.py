"""907. Sum of Subarray Minimums
https://leetcode.com/problems/sum-of-subarray-minimums/
"""
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        base = int(1e9 + 7)
        stack = []
        ans = 0
        for r in range(len(arr) + 1):
            t = arr[r] if r < len(arr) else 0
            while stack and arr[stack[-1]] >= t:
                cur = stack.pop()
                l = stack[-1] if stack else -1
                ans = (ans + (cur - l) * (r - cur) * arr[cur]) % base
            stack.append(r)
        return ans
