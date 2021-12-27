"""825. Friends Of Appropriate Ages
https://leetcode.com/problems/friends-of-appropriate-ages/

n == ages.length
1 <= n <= 2 * 10^4
1 <= ages[i] <= 120

age[y] <= 0.5 * age[x] + 7
age[y] > age[x]
age[y] > 100 && age[x] < 100
"""
from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def helper(x: int, y: int) -> bool:
            if y <= 0.5 * x + 7:
                return False
            if y > x:
                return False
            if y > 100 and x < 100:
                return False
            return True

        ans = 0
        n = len(ages)
        ages.sort()
        l, r = 0, 0
        for i in range(n):
            while i > l and not helper(ages[l], ages[i]):
                i += 1
            if r < i:
                r = i
            while r < n and helper(ages[r], ages[i]):
                r += 1
            if r > l:
                ans += r - l - 1
        return ans
