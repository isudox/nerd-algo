"""486. Predict the Winner
https://leetcode.com/problems/predict-the-winner/
"""
from typing import List


class Solution:
    def predict_the_winner(self, nums: List[int]) -> bool:
        def helper(i: int, j: int) -> int:
            if i == j:
                return nums[i]
            return max(nums[i] - helper(i + 1, j), nums[j] - helper(i, j - 1))

        return helper(0, len(nums) - 1) >= 0
