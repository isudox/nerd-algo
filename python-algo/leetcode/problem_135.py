"""135. Candy
https://leetcode.com/problems/candy/

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.

What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.
"""
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        def help(start: int, end: int, step: int) -> List[int]:
            candies = [0] * n
            candies[start] = 1
            for i in range(start + step, end, step):
                if ratings[i] > ratings[i - step]:
                    candies[i] = candies[i - step] + 1
                else:
                    candies[i] = 1
            return candies
        n = len(ratings)
        candies_left = help(0, n, 1)
        candies_right = help(n - 1, -1, -1)
        ans = 0
        for i in range(n):
            ans += max(candies_left[i], candies_right[i])
        return ans
