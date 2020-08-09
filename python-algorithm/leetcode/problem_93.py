"""93. Restore IP Addresses
https://leetcode.com/problems/restore-ip-addresses/

Given a string containing only digits, restore it by returning
all possible valid IP address combinations.

A valid IP address consists of exactly four integers
(each integer is between 0 and 255) separated by single points.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""
from typing import List


class Solution:
    def restore_ip_addresses(self, s: str) -> List[str]:
        def dfs(pos: int, count: int, ip: str):
            m = len(s) - pos  # count * 1 <= m <= count*3
            if m < count or m > count * 3:
                return
            if m == 0 and count == 0:
                ans.append(ip)
                return
            next_pos = pos + 1
            while next_pos <= pos + 3:
                cur_num = s[pos:next_pos]
                if 0 <= int(cur_num) <= 255:
                    dfs(next_pos, count - 1,
                        (ip + '.' + cur_num) if count < 4 else cur_num)
                    if cur_num == '0':
                        break
                next_pos += 1

        ans = []
        dfs(0, 4, "")
        return ans
