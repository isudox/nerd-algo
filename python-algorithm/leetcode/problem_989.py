"""989. Add to Array-Form of Integer
https://leetcode.com/problems/add-to-array-form-of-integer/
"""
from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        def merge(a: List[int], b: List[int]) -> List[int]:
            add = 0
            for i in range(len(a)):
                cur = a[len(a) - 1 - i] + add + (b[len(b) - 1 - i] if i < len(b) else 0)
                add, cur = divmod(cur, 10)
                a[len(a) - 1 - i] = cur
            return [1] + a if add else a

        k_num = []
        while k:
            k_num.insert(0, k % 10)
            k //= 10
        return merge(num, k_num) if len(num) >= len(k_num) else merge(k_num, num)

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

