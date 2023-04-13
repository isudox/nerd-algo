"""1041. Robot Bounded In Circle
https://leetcode.com/problems/robot-bounded-in-circle/
"""


def is_robot_bounded(instructions: str) -> bool:
    dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]  # N,S,W,E
    p = [0, 0, 0]
    for instruction in instructions:
        d = p[2]
        if instruction == 'G':
            p[0] += dirs[d][0]
            p[1] += dirs[d][1]
        elif d == 0:
            p[2] = 2 if instruction == 'L' else 3
        elif d == 1:
            p[2] = 3 if instruction == 'L' else 2
        elif d == 2:
            p[2] = 1 if instruction == 'L' else 0
        else:
            p[2] = 0 if instruction == 'L' else 1
    if p[2] != 0 or p == [0, 0, 0]:
        return True
    return False
