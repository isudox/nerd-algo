"""859. Buddy Strings
https://leetcode.com/problems/buddy-strings/
"""
import collections


class Solution:
    def buddy_strings(self, s: str, goal: str) -> bool:
        n, m = len(s), len(goal),
        if n != m:
            return False
        if s == goal:
            counter = collections.Counter(s)
            for ch, cnt in counter.items():
                if cnt >= 2:
                    return True
            return False
        memo = []
        for i in range(n):
            if s[i] != goal[i]:
                memo.append(i)
        if len(memo) != 2:
            return False
        return s[memo[0]] == goal[memo[1]] and s[memo[1]] == goal[memo[0]]
