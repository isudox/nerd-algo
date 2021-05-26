"""546. Remove Boxes
https://leetcode.com/problems/remove-boxes/

You are given several boxes with different colors represented by different
positive numbers.

You may experience several rounds to remove boxes until there is no box left.
Each time you can choose some continuous boxes with the same color (i.e.,
composed of k boxes, k >= 1), remove them and get k * k points.

Return the maximum points you can get.

Example 1:

Input: boxes = [1,3,2,2,2,3,4,3,1]
Output: 23
Explanation:
[1, 3, 2, 2, 2, 3, 4, 3, 1]
----> [1, 3, 3, 4, 3, 1] (3*3=9 points)
----> [1, 3, 3, 3, 1] (1*1=1 points)
----> [1, 1] (3*3=9 points)
----> [] (2*2=4 points)

Example 2:

Input: boxes = [1,1,1]
Output: 9

Example 3:

Input: boxes = [1]
Output: 1

Constraints:

1 <= boxes.length <= 100
1 <= boxes[i] <= 100
"""
from typing import List


class Solution:
    def remove_boxes(self, boxes: List[int]) -> int:
        @lru_cache(None)
        def helper(l: int, r: int, k: int) -> int:
            if l > r:
                return 0
            while r > l and boxes[r] == boxes[r-1]:
                r -= 1
                k += 1
            res = helper(l, r-1, 0) + (k+1)**2
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    res = max(res, helper(l, i, k+1) + helper(i+1, r-1, 0))
            return res

        return helper(0, len(boxes) - 1, 0)
