"""321. Create Maximum Number
https://leetcode.com/problems/create-maximum-number/

Given two arrays of length m and n with digits 0-9 representing two numbers.
Create the maximum number of length k <= m + n from digits of the two.
The relative order of the digits from the same array must be preserved.
Return an array of the k digits.

Note: You should try to optimize your time and space complexity.

Example 1:

Input:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
Output:
[9, 8, 6, 5, 3]

Example 2:

Input:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
Output:
[6, 7, 6, 0, 4]

Example 3:

Input:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
Output:
[9, 8, 9]
"""
from typing import List

# TODO
class Solution:
    def max_number(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def max_from_list(nums: List[int], k: int) -> List[int]:
            n = len(nums)
            if k >= n:
                return nums
            max_list = [nums[0]]
            dropped = 0
            for i in range(1, n):
                if nums[i] <= max_list[-1]:
                    max_list.append(i)
                else:
                    cur_len = len(max_list)
                    for j in range(cur_len - 1, n - k - dropped, -1):
                        pass

            return max_list

        maximum = 0

        return []


if __name__ == '__main__':
    sol = Solution()
    print(sol.max_number([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5))
