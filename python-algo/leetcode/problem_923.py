"""923. 3Sum With Multiplicity
https://leetcode.com/problems/3sum-with-multiplicity/
"""
import collections
from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        def helper(start: int, tar: int) -> int:
            if arr[start] * 2 > tar:
                return 0
            ret = 0
            memo = collections.defaultdict(int)
            for x in range(start, n):
                if (tar - arr[x]) in memo:
                    ret += memo[tar - arr[x]]
                memo[arr[x]] += 1
            return ret % mod

        mod = 1000000007
        arr.sort()
        n = len(arr)
        ans = 0
        for i in range(n - 2):
            if arr[i] * 3 > target:
                break
            cnt = helper(i + 1, target - arr[i])
            ans = (ans + cnt) % mod
        return ans
