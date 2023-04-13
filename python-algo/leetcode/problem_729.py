"""729. My Calendar I
https://leetcode.com/problems/my-calendar-i
"""
from bisect import bisect_left


class MyCalendar:

    def __init__(self):
        self.calendars = []

    def book(self, start: int, end: int) -> bool:
        i = bisect_left(self.calendars, (start, end))
        is_left_valid = i == 0 or self.calendars[i - 1][1] <= start
        is_right_valid = i == len(self.calendars) or end <= self.calendars[i][0]
        if is_left_valid and is_right_valid:
            self.calendars.insert(i, (start, end))
            return True
        return False
