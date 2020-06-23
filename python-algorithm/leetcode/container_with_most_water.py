"""11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/

Given n non-negative integers a1, a2, ..., an , where each represents a point
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""
from typing import List


class Solution:
    def max_area(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        ans = 0
        while i < j:
            if i > 1 and height[i] <= height[i - 1]:
                i += 1
                continue
            if j < len(height) - 2 and height[j] < height[j + 1]:
                j -= 1
                continue
            h = min(height[i], height[j])
            cur = h * (j - i)
            ans = max(cur, ans)
            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else:
                i += 1
                j -= 1
        return ans
