"""1300. Sum of Mutated Array Closest to Target
https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/

Given an integer array arr and a target value target, return the integer value
such that when we change all the integers larger than value in the given array
to be equal to value, the sum of the array gets as close as possible
(in absolute difference) to target.

In case of a tie, return the minimum such integer.

Notice that the answer is not neccesarilly a number from arr.


Example 1:

Input: arr = [4,9,3], target = 10
Output: 3
Explanation: When using 3 arr converts to [3, 3, 3] which sums 9
and that's the optimal answer.


Example 2:

Input: arr = [2,3,5], target = 10
Output: 5


Example 3:

Input: arr = [60864,25176,27249,21296,20204], target = 56803
Output: 11361


Constraints:

1 <= arr.length <= 10^4
1 <= arr[i], target <= 10^5
"""
from typing import List


class Solution:
    def find_best_value(self, arr: List[int], target: int) -> int:
        def binary_search(nums: List[int], value) -> int:
            start, end = 0, len(nums)
            while start < end:
                mid = start + (end - start) // 2
                if nums[mid] < value:
                    start = mid + 1
                else:
                    end = mid
            return start

        arr.sort()
        n = len(arr)
        diff = target
        result = 0
        sum_store = [0]
        for num in arr:
            sum_store.append(num + sum_store[-1])
        for x in range(1, arr[-1] + 1):
            index = binary_search(arr, x)
            cur_sum = (n - index) * x + sum_store[index]
            if abs(cur_sum - target) < diff:
                diff = abs(cur_sum - target)
                result = x
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.find_best_value([4, 9, 3], 10))
