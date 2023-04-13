"""
There is a robot starting at position (0, 0), the origin, on a 2D plane.
Given a sequence of its moves, judge if this robot ends up at (0, 0) after
it completes its moves.

The move sequence is represented by a string, and the character moves[i]
represents its ith move. Valid moves are R (right), L (left), U (up),
and D (down). If the robot returns to the origin after it finishes all of
its moves, return true. Otherwise, return false.

Note: The way that the robot is "facing" is irrelevant. "R" will always make
the robot move to the right once, "L" will always make it move left, etc.
Also, assume that the magnitude of the robot's movement is the same for each move.

Example 1:

Input: "UD"
Output: true
"""
from typing import List


class Solution:
    def judge_circle_2(self, moves: str) -> bool:
        def process(stack: List[str], char: str):
            if not stack or stack[-1] == char:
                stack.append(char)
            else:
                stack.pop(-1)

        pairs = {"L": 0, "R": 0, "U": 1, "D": 1}
        stacks = [[], []]
        for c in moves:
            process(stacks[pairs[c]], c)
        return not stacks[0] and not stacks[1]

    def judge_circle(self, moves: str) -> bool:
        dirs = {"L": [0, -1], "R": [0, 1], "U": [-1, 0], "D": [1, 0]}
        loc = [0, 0]
        for move in moves:
            d = dirs[move]
            loc[0], loc[1] = loc[0] + d[0], loc[1] + d[1],
        return loc == [0, 0]
