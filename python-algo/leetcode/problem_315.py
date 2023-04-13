"""315. Count of Smaller Numbers After Self
https://leetcode.com/problems/count-of-smaller-numbers-after-self/

You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller
elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
"""
from typing import List


class Solution:
    def count_smaller_0(self, nums: List[int]) -> List[int]:
        """
        brute force
        time complexity: O(N^2)
        space complexity: O(N)
        """
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            count = 0
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    count += 1
            ans[i] = count
        return ans

    def count_smaller_1(self, nums: List[int]) -> List[int]:
        def binary_search(arr: List[int], target: int) -> int:
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if arr[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        n = len(nums)
        ans = [0] * n
        sorted_nums = []
        for i in range(n - 1, -1, -1):
            index = binary_search(sorted_nums, nums[i])
            ans[i] = index
            sorted_nums.insert(index, nums[i])
        return ans
