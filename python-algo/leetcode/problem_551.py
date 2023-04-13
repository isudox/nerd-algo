"""551. Student Attendance Record I
https://leetcode.com/problems/student-attendance-record-i/
"""


class Solution:
    def check_record(self, s: str) -> bool:
        l_cnt, a_cnt = 0, 0
        pre = ''
        for c in s:
            if c == 'L':
                l_cnt += 1
                if l_cnt == 3:
                    return False
            elif pre == 'L':
                l_cnt = 0
            if c == 'A':
                a_cnt += 1
                if a_cnt == 2:
                    return False
            pre = c
        return True

