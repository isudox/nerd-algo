"""658. Find K Closest Elements
https://leetcode.com/problems/find-k-closest-elements/
"""
import heapq
from bisect import bisect_left
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pos = bisect_left(arr, x)
        pq = []
        for i in range(max(0, pos - k), min(pos + k, len(arr))):
            heapq.heappush(pq, CustomTuple(arr[i], abs(arr[i] - x)))
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(pq).x)
        ans.sort()
        return ans

    def findClosestElements2(self, arr: List[int], k: int, x: int) -> List[int]:
        ans = []
        for i in range(len(arr)):
            if len(ans) < k:
                ans.append(arr[i])
            else:
                cur_diff = abs(arr[i] - x)
                if cur_diff < abs(ans[0] - x):
                    ans.pop(0)
                    ans.append(arr[i])
                elif arr[i] > ans[0]:
                    break
        return ans

    def findClosestElements3(self, arr: List[int], k: int, x: int) -> List[int]:
        pos = bisect_left(arr, x)
        ans = []
        for i in range(max(0, pos - k), min(pos + k, len(arr))):
            if len(ans) < k:
                ans.append(arr[i])
            else:
                cur_diff = abs(arr[i] - x)
                if cur_diff < abs(ans[0] - x):
                    ans.pop(0)
                    ans.append(arr[i])
                elif arr[i] > ans[0]:
                    break
        return ans


class CustomTuple:
    def __init__(self, x: int, d: int):
        self.x = x
        self.d = d

    def __lt__(self, that):
        return self.x < that.x if self.d == that.d else self.d < that.d
