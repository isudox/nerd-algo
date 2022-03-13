"""393. UTF-8 Validation
https://leetcode.com/problems/utf-8-validation/
"""
from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        bin_nums = []
        for num in data:
            bin_num = bin(num)[2:]
            bin_num = '0' * (8 - len(bin_num)) + bin_num
            bin_nums.append(bin_num)
        i, n = 0, len(data)
        while i < n:
            bin_num = bin_nums[i]
            if bin_num[0] == '0':  # 表示 1 字节
                i += 1
                continue
            j = 0
            while j < len(bin_num) and bin_num[j] == '1':
                j += 1
            if j == 1 or j > 4:  # 只有 1 字节或超过 4 字节
                return False
            if i + j > n:  # 超过给定的二进制个数
                return False
            for k in range(i + 1, i + j):
                if bin_nums[k][:2] != '10':
                    return False
            i += j
        return True
