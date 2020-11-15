"""1122. Relative Sort Array
https://leetcode.com/problems/relative-sort-array/

Given two arrays arr1 and arr2, the elements of arr2 are distinct,
and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1
are the same as in arr2.
Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

Constraints:

    arr1.length, arr2.length <= 1000
    0 <= arr1[i], arr2[i] <= 1000
    Each arr2[i] is distinct.
    Each arr2[i] is in arr1.
"""
from typing import List


class Solution:
    def relative_sort_array(self, arr1: List[int], arr2: List[int]) -> List[int]:
        num_dict = dict.fromkeys(arr2, True)
        positions = [0] * 1001
        counter = {}
        for num in arr1:
            if num in num_dict:
                counter[num] = 1 + (counter[num] if num in counter else 0)
            else:
                positions[num] += 1
        ans = []
        for num in arr2:
            ans.extend([num] * counter[num])
        for i in range(1001):
            if positions[i] > 0:
                ans.extend([i] * positions[i])
        return ans

    def relative_sort_array_2(self, arr1: List[int], arr2: List[int]) -> List[int]:
        positions = [0] * 1001
        for num in arr1:
            positions[num] += 1
        left, right = [], []
        for num in arr2:
            left.extend([num] * positions[num])
            positions[num] = 0
        for num in range(1001):
            if positions[num] > 0:
                right.extend([num] * positions[num])
        return left + right


if __name__ == '__main__':
    sol = Solution()
    a1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    a2 = [2, 1, 4, 3, 9, 6]
    print(sol.relative_sort_array(a1, a2))
    print(sol.relative_sort_array_2(a1, a2))
