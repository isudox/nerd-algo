"""390. Elimination Game
https://leetcode.com/problems/elimination-game/
"""


def last_remaining(n: int) -> int:
    ans = 1
    step = 1
    cnt = n
    flag = True  # left -> right
    while cnt > 1:
        if flag:
            ans += step
        elif cnt % 2 == 1:
            ans += step
        flag = not flag
        step = step * 2
        cnt = cnt // 2
    return ans
