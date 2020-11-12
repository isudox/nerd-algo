"""347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

Note:

    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
    It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
    You can return the answer in any order.
"""
from typing import List


class Solution:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = 1 + (counter[num] if num in counter else 0)
        n = len(nums)
        store = [[] for _ in range(n + 1)]
        for num, count in counter.items():
            store[count].append(num)
        ans = []
        for i in range(n, -1, -1):
            if store[i]:
                ans.extend(store[i])
                k -= len(store[i])
                if k == 0:
                    break
        return ans

    def top_k_frequent_2(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        n = len(nums)
        store = [[] for _ in range(n + 1)]
        pre, cnt = None, 0
        for num in nums:
            if pre is None:
                cnt = 1
                pre = num
            else:
                if num == pre:
                    cnt += 1
                else:
                    store[cnt].append(pre)
                    cnt = 1
                    pre = num
        store[cnt].append(pre)
        ans = []
        for i in range(n, -1, -1):
            if store[i]:
                ans.extend(store[i])
                k -= len(store[i])
                if k == 0:
                    break
        return ans
