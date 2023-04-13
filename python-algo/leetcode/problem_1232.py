"""1232. Check If It Is a Straight Line
https://leetcode.com/problems/check-if-it-is-a-straight-line/
"""
from typing import List


class Solution:
    def check_straight_line(self, coordinates: List[List[int]]) -> bool:
        def helper(p1: List[int], p2: List[int], mode: bool, k: float) -> bool:
            if mode:
                if p2[1] - p1[1] != 0:
                    return (p2[0] - p1[0]) / (p2[1] - p1[1]) == k
                return False
            else:
                if p2[0] - p1[0] != 0:
                    return (p2[1] - p1[1]) / (p2[0] - p1[0]) == k
                return False

        n = len(coordinates)
        if n <= 2:
            return True
        delta_x = coordinates[1][0] - coordinates[0][0]
        delta_y = coordinates[1][1] - coordinates[0][1]
        flag = coordinates[1][0] - coordinates[0][0] == 0
        if flag:
            k = delta_x / delta_y
        else:
            k = delta_y / delta_x
        for i in range(2, n):
            if not helper(coordinates[i], coordinates[i - 1], flag, k):
                return False
        return True
