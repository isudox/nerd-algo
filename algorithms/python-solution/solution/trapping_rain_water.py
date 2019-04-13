"""42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/description/


Given n non-negative integers representing an elevation map where the width
of each bar is 1, compute how much water it is able to trap after raining.

![img](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
this case, 6 units of rain water (blue section) are being trapped. Thanks
Marcos for contributing this image!

Example:


Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
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


if __name__ == "__main__":
    solution = Solution()
    print(solution.trap([2, 1, 0, 1, 3]))
    print(solution.trap([3, 2, 1, 2, 1]))
    print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(solution.trap([4, 2, 3]))
