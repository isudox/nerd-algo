"""444. Sequence Reconstruction
https://leetcode.com/problems/sequence-reconstruction/
"""
from typing import List


class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        n = len(nums)
        seen = [False] * n
        seen[0] = True
        positions = [0] * (n + 1)
        for i, num in enumerate(nums):
            positions[num] = i
        for seq in sequences:
            for i in range(1, len(seq)):
                d = positions[seq[i]] - positions[seq[i - 1]]
                if d == 1:
                    seen[positions[seq[i]]] = True
                elif d < 0:
                    return False
        for val in seen:
            if not val:
                return False
        return True
