"""93. Restore IP Addresses
https://leetcode.com/problems/restore-ip-addresses/
"""
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(ip: str, i: int, need: int):
            n = len(s) - i
            if n < need or n > need * 3:
                return
            if i == len(s) and need == 0:
                ans.append(ip[1:])
                return
            if s[i] == '0':
                backtrack(ip + '.0', i + 1, need - 1)
                return
            for j in range(1, 4):
                num = s[i:i + j]
                if 0 <= int(num) <= 255:
                    backtrack(ip + '.' + num, i + j, need - 1)

        ans = []
        backtrack('', 0, 4)
        return ans

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
