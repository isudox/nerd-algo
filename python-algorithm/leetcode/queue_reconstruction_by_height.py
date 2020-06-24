"""406. Queue Reconstruction by Height
https://leetcode.com/problems/queue-reconstruction-by-height/

Suppose you have a random list of people standing in a queue.
Each person is described by a pair of integers (h, k),
where h is the height of the person and k is the number of people
in front of this person who have a height greater than or equal to h.
Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""
from typing import List


class Solution:
    def reconstruct_queue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(reverse=True)
        # [[7, 1], [7, 0], [6, 1], [5, 2], [5, 0], [4, 4]]
        ans = [people[0]]
        for i in range(1, len(people)):
            if people[i][]
        return ans
