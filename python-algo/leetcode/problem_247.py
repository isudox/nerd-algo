"""247. Strobogrammatic Number II
https://leetcode.com/problems/strobogrammatic-number-ii/

Given an integer n, return all the strobogrammatic numbers that
are of length n. You may return the answer in any order.

A strobogrammatic number is a number that looks the same when
rotated 180 degrees (looked at upside down).

Example 1:

Input: n = 2
Output: ["11","69","88","96"]
Example 2:

Input: n = 1
Output: ["0","1","8"]

Constraints:

1 <= n <= 14
"""
from typing import List


class Solution:
    def find_strobogrammatic(self, n: int) -> List[str]:
        def helper(k: int) -> List[str]:
            list1 = ["0", "1", "8"]
            list2 = ["00", "11", "69", "88", "96"]
            if k == 1:
                return list1
            if k == 2:
                return list2
            ret = []
            prev = k - 2 if k % 2 == 0 else k - 1
            split = prev // 2
            prev_list = helper(prev)
            for num in prev_list:
                for interval in (list2 if k % 2 == 0 else list1):
                    ret.append(num[:split] + interval + num[split:])
            return ret

        ans = helper(n)
        ans = [num for num in ans if len(num) == 1 or not num.startswith('0')]
        return ans

