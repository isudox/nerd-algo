"""189. Rotate Array
https://leetcode.com/problems/rotate-array/

Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

    Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
    Could you do it in-place with O(1) extra space?

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:

    1 <= nums.length <= 2 * 10^4
    -2^31 <= nums[i] <= 2^31 - 1
    0 <= k <= 10^5
"""
from typing import List


class Solution:
    def rotate_1(self, nums: List[int], k: int) -> None:
        n = len(nums)
        new_nums = nums[n - k:] + nums[:n - k]
        for i in range(n):
            nums[i] = new_nums[i]

    def rotate_2(self, nums: List[int], k: int) -> None:
        def helper(x: int, cur: int, ops: int, total_ops: int):
            if ops == total_ops:
                return
            x = (x + k) % n
            temp, nums[x] = nums[x], cur
            helper(x, temp, ops + 1, total_ops)

        n = len(nums)
        k = k % n
        if k == 0:
            return
        if n % k != 0 and n % (n - k) != 0:
            helper(0, nums[0], 0, n)
        else:
            for i in range(min(k, n - k)):
                helper(i, nums[i], 0, n // min(k, n - k))

    def rotate_3(self, nums: List[int], k: int) -> None:
        def get_gcd(a: int, b: int) -> int:
            return get_gcd(b, a % b) if b > 0 else a

        def helper(x: int, cur: int, ops: int, total_ops: int):
            if ops == total_ops:
                return
            x = x + k if x + k < n else x + k - n
            temp, nums[x] = nums[x], cur
            helper(x, temp, ops + 1, total_ops)

        n = len(nums)
        k = k % n
        if k == 0:
            return
        gcd = get_gcd(n, k)  # greatest common divisor of (n, k)
        for i in range(gcd):
            helper(i, nums[i], 0, n // gcd)

    def rotate_4(self, nums: List[int], k: int) -> None:
        def get_gcd(a: int, b: int) -> int:
            return get_gcd(b, a % b) if b > 0 else a

        n = len(nums)
        k = k % n
        if k == 0:
            return
        gcd = get_gcd(n, k)
        for i in range(gcd):
            idx = i
            prev = nums[i]
            while True:
                idx = (idx + k) % n
                temp = nums[idx]
                nums[idx], prev = prev, temp
                if idx == i:
                    break

    def rotate_5(self, nums: List[int], k: int) -> None:
        def helper(start: int, end: int):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)
        k = k % n
        if k == 0:
            return
        helper(0, n - 1)
        helper(0, k - 1)
        helper(k, n - 1)
