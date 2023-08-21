"""239. Sliding Window Maximum
https://leetcode.com/problems/sliding-window-maximum/
"""
from typing import List
from collections import deque


class Solution:
    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        """
        brute force
        """
        if not nums or not k:
            return []
        n = len(nums)
        ans = []
        for i in range(n - k + 1):
            ans.append(max(nums[i:i + k]))
        return ans

    def max_sliding_window_2(self, nums: List[int], k: int) -> List[int]:
        def clean_deque(idx: int):
            if dq and dq[0] == idx - k:
                dq.popleft()
            while dq and nums[idx] > nums[dq[-1]]:
                dq.pop()
        if not nums or not k:
            return []
        dq = deque()
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            dq.append(i)
            if nums[i] > nums[max_idx]:
                max_idx = i
        ans = [nums[max_idx]]
        for i in range(k, len(nums)):
            clean_deque(i)
            dq.append(i)
            ans.append(nums[dq[0]])
        return ans


class MaxHeap:
    def __init__(self, arr: List[int] = None):
        self.arr = arr
        self._heapify()

    def add(self, val: int):
        pass

    def remove(self, val: int):
        pass

    def _heapify(self):
        pass

    def top(self):
        return self.arr[0]
