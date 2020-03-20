"""739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/

Given a list of daily temperatures T, return a list such that, for each day
in the input, tells you how many days you would have to wait until a warmer
temperature. If there is no future day for which this is possible,
put 0 instead.

For example, given the list of temperatures
T = [73, 74, 75, 71, 69, 72, 76, 73],
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100].
"""
from typing import List


class Solution:
    def brute_force(self, t: List[int]) -> List[int]:
        n = len(t)
        if n == 1:
            return [0]
        result = []
        for i in range(n):
            for j in range(i + 1, n + 1):
                if j == n:
                    result.append(0)
                    break
                if t[j] <= t[i]:
                    j += 1
                else:
                    result.append(j - i)
                    break
        return result

    def daily_temperatures(self, t: List[int]) -> List[int]:
        """
        costs too much time, not ac.
        """
        n = len(t)
        result = [0 for _ in range(n)]
        up_points = []
        for i in range(1, n):
            if t[i] > t[i - 1]:
                up_points.append(i)
                result[i - 1] = 1
        for j in range(n):
            if result[j] > 0:
                continue
            for up_point in up_points:
                if up_point > j:
                    if t[up_point] > t[j]:
                        result[j] = up_point - j
                        break
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.daily_temperatures([5, 3, 0, 1, 2]))
    print(s.daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    print(s.daily_temperatures([9, 8, 7, 6, 5, 4, 3, 2, 1]))
