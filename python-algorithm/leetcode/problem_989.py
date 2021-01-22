"""989. Add to Array-Form of Integer
https://leetcode.com/problems/add-to-array-form-of-integer/

For a non-negative integer X, the array-form of X is an array of its digits
in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.

Example 1:

Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234

Example 2:

Input: A = [2,7,4], K = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455

Example 3:

Input: A = [2,1,5], K = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021

Example 4:

Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
Output: [1,0,0,0,0,0,0,0,0,0,0]
Explanation: 9999999999 + 1 = 10000000000

Note：

    1 <= A.length <= 10000
    0 <= A[i] <= 9
    0 <= K <= 10000
    If A.length > 1, then A[0] != 0
"""
from typing import List


class Solution:
    def add_to_array_form(self, a: List[int], k: int) -> List[int]:
        def helper(long_list: List[int], short_list: List[int]) -> List[int]:
            len_short, len_long = len(short_list), len(long_list)
            i = 1
            prev = 0
            while len_short - i >= 0:
                cur = long_list[len_long - i] + short_list[len_short - i] + prev
                prev, cur = divmod(cur, 10)
                long_list[len_long - i] = cur
                i += 1
            while prev and len_long - i >= 0:
                cur = long_list[len_long - i] + prev
                prev, cur = divmod(cur, 10)
                long_list[len_long - i] = cur
                i += 1
            if prev == 1:
                long_list.insert(0, 1)
            return long_list

        list_k = [int(c) for c in str(k)]
        len_k, len_a = len(list_k), len(a)
        if len_a < len_k:
            return helper(list_k, a)
        return helper(a, list_k)

    def add_to_array_form_2(self, a: List[int], k: int) -> List[int]:
        def helper(list_1: List[int], list_2: List[int]) -> List[int]:
            n = len(list_1)
            prev = 0
            for i in range(n):
                index = n - 1 - i
                cur = list_1[index] + list_2[index] + prev
                prev, cur = divmod(cur, 10)
                list_1[index] = cur
            if prev == 1:
                list_1.insert(0, 1)
            return list_1

        list_k = [int(c) for c in str(k)]
        len_k, len_a = len(list_k), len(a)
        if len_k < len_a:
            list_k = [0] * (len_a - len_k) + list_k
        else:
            a = [0] * (len_k - len_a) + a
        return helper(a, list_k)


if __name__ == '__main__':
    sol = Solution()
    print(sol.add_to_array_form_2([0], 123))
