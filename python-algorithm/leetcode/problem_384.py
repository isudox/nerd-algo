"""384. Shuffle an Array
https://leetcode.com/problems/shuffle-an-array/

Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result.
Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
"""
from typing import List
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.origin = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.origin

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        n = len(self.origin)
        new_nums = []
        used = []
        for i in range(n):
            while True:
                r = random.randint(0, n - 1)
                if r not in used:
                    used.append(r)
                    new_nums.append(self.origin[r])
                    break
        return new_nums


if __name__ == '__main__':
    s = Solution([-6, 10, 184])
    print(s.shuffle())
    print(s.reset())
    print(s.shuffle())

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
