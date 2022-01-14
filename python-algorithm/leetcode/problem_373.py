"""373. Find K Pairs with Smallest Sums
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
"""
import heapq
from typing import List


def k_smallest_pairs(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    m, n = len(nums1), len(nums2),
    ans = []
    pq = []
    for i in range(min(k, m)):
        heapq.heappush(pq, (nums1[i] + nums2[0], i, 0))
    while pq and len(ans) < k:
        t, i, j = heapq.heappop(pq)
        ans.append([nums1[i], nums2[j]])
        if j < n - 1:
            heapq.heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
    return ans
