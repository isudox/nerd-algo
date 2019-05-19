"""66. Plus One
https://leetcode.com/problems/plus-one/


Given a non-empty array of digits representing a non-negative integer,
plus one to the integer.

The digits are stored such that the most significant digit is at the head of
the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero,
except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.


Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""
from typing import List


class Solution:
    def plus_one(self, digits: List[int]) -> List[int]:
        num = 0
        for digit in digits:
            num = num * 10 + digit
        num += 1
        return [int(x) for x in str(num)]

    def plus_one_2(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        gt_ten = True
        while gt_ten and i >= 0:
            if i == 0 and digits[i] == 9:
                digits[i] = 0
                digits.insert(0, 1)
                break
            digits[i] += 1
            if digits[i] >= 10:
                digits[i] -= 10
            else:
                gt_ten = False
            i -= 1
        return digits
