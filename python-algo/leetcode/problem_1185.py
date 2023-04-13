"""1185. Day of the Week
https://leetcode.com/problems/day-of-the-week/
"""


def day_of_the_week(day: int, month: int, year: int) -> str:
    store = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    days_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    cnt = 3
    for y in range(1970, year):
        cnt += 365
        if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
            cnt += 1
    for m in range(1, month):
        cnt += days_of_month[m]
        if m == 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            cnt += 1
    cnt += day
    return store[cnt % 7]
