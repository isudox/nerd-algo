"""632. Smallest Range Covering Elements from K Lists
https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

You have k lists of sorted integers in ascending order.
Find the smallest range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

Example 1:

Input: [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation:
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].

Note:

The given list may contain duplicates, so ascending order means >= here.
1 <= k <= 3500
-105 <= value of elements <= 105.
"""
import collections
import sys
import heapq
from typing import List


class Solution:
    def smallest_range(self, nums: List[List[int]]) -> List[int]:
        indices = collections.defaultdict(list)
        max_num, min_num = 1 - sys.maxsize, sys.maxsize
        for i, li in enumerate(nums):
            for num in li:
                indices[num].append(i)
            min_num = min(min_num, min(li))
            max_num = max(max_num, max(li))

        left, right = min_num, max_num
        l_slide, r_slide = min_num, min_num - 1  # sliding window
        freq = [0] * len(nums)
        inside = 0

        while r_slide < max_num:
            r_slide += 1
            if r_slide in indices:
                for x in indices[r_slide]:
                    freq[x] += 1
                    if freq[x] == 1:
                        inside += 1
                while inside == len(nums):
                    if r_slide - l_slide < right - left:
                        left, right = l_slide, r_slide
                    if l_slide in indices:
                        for x in indices[l_slide]:
                            freq[x] -= 1
                            if freq[x] == 0:
                                inside -= 1
                    l_slide += 1

        return [left, right]

    def smallest_range_2(self, nums: List[List[int]]) -> List[int]:
        # pick a num from each list, and make the value of (max - min) minimum.
        left, right = 1 - sys.maxsize, sys.maxsize
        max_num = max(li[0] for li in nums)
        pq = [(li[0], i, 0) for i, li in enumerate(nums)]
        heapq.heapify(pq)

        while True:
            min_num, x, y = heapq.heappop(pq)
            if max_num - min_num < right - left:
                left, right = min_num, max_num
            if y == len(nums[x]) - 1:
                break
            max_num = max(max_num, nums[x][y + 1])
            heapq.heappush(pq, (nums[x][y + 1], x, y + 1))

        return [left, right]
