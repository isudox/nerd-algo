"""42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/description/
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ans, left = 0, 0
        stack = []
        for h in height:
            if not stack:
                stack.append(h)
                left = h
            elif h < left:
                if h <= stack[-1]:
                    stack.append(h)
                else:
                    cnt = 0
                    while stack[-1] < h:
                        ans += h - stack.pop()
                        cnt += 1
                        if not stack:
                            break
                    stack.extend([h] * (cnt + 1))
            else:
                top = min(left, h)
                ans += len(stack) * top - sum(stack)
                stack.clear()
                stack.append(h)
                left = h

        return ans
