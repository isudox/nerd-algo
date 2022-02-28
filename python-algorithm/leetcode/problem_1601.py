"""1601. Maximum Number of Achievable Transfer Requests
https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/
"""
from typing import List


def maximum_requests(n: int, requests: List[List[int]]) -> int:
    def helper(x: int) -> int:
        cnt = 0
        counter = [0] * n
        for i in range(len(requests)):
            bit = x & 1
            x = x >> 1
            if bit:
                cnt += 1
                from_i, to_i = requests[i]
                counter[from_i] -= 1
                counter[to_i] += 1
        for c in counter:
            if c != 0:
                return -1
        return cnt

    ans = 0
    limit = 1 << (len(requests))
    for i in range(0, limit):
        ret = helper(i)
        if ret > ans:
            ans = ret
    return ans
