"""552. Student Attendance Record II
https://leetcode.com/problems/student-attendance-record-ii/
"""
from functools import lru_cache


class Solution:
    def check_record(self, n: int) -> int:
        @lru_cache(None)
        def dfs(pos: int, a_cnt: int, l_cnt: int) -> int:
            if a_cnt == 2 or l_cnt == 3:
                return 0
            if pos == n:
                return 1
            ret = 0
            ret += dfs(pos + 1, a_cnt + 1, 0) % base
            ret += dfs(pos + 1, a_cnt, l_cnt + 1) % base
            ret += dfs(pos + 1, a_cnt, 0) % base
            return ret % base

        base = int(1e9 + 7)
        return dfs(0, 0, 0)
