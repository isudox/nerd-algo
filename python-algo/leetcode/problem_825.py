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
        ans = 0
        n = len(ages)
        ages.sort()
        l, r = 0, 0
        for age in ages:
            if age < 15:
                continue
            while ages[l] <= 0.5 * age + 7:
                l += 1
            while r + 1 < n and ages[r + 1] <= age:
                r += 1
            ans += r - l
        return ans
