"""1104. Path In Zigzag Labelled Binary Tree
https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/
"""
from typing import List
import math


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans = []
        row = int(math.log2(label)) + 1
        while row > 0:
            ans.insert(0, label)
            label = 2 ** (row - 2) * 3 - 1 - label // 2
            row -= 1
        return ans
