"""1154. Day of the Year
https://leetcode.com/problems/day-of-the-year/
"""


class Solution:
    def dayOfYear(self, date: str) -> int:
        store = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year, month, day = [int(_) for _ in date.split('-')]
        isleap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        ans = 0
        for i in range(month):
            ans += store[i]
            if isleap and i == 2:
                ans += 1
        ans += day
        return ans
