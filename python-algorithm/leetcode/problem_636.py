"""636. Exclusive Time of Functions
https://leetcode.com/problems/exclusive-time-of-functions/
"""
from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []
        for log in logs:
            log_seg = log.split(":")
            fid, flag, ts = int(log_seg[0]), log_seg[1], int(log_seg[2])
            if not stack:
                stack.append([fid, flag, ts])
            elif flag == 'start':
                pre_fid, pre_flag, pre_ts = stack[-1]
                ans[pre_fid] += ts - pre_ts
                stack.append([fid, flag, ts])
            else:
                pre_fid, pre_flag, pre_ts = stack.pop()
                ans[pre_fid] += ts - pre_ts + 1
                if stack:
                    stack[-1][2] = ts + 1
        return ans
